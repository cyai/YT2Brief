from yt2brief.transcribe import Transcribe
from yt2brief.fromat import Reformat

# from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from functools import partial

from langchain.chains.combine_documents import collapse_docs, split_list_of_docs
from langchain.chains.combine_documents import collapse_docs
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough
from langchain.schema import Document
from langchain.llms import Replicate

import os
from dotenv import load_dotenv
import json
import yaml

load_dotenv()


class Summarize:
    def __init__(self) -> None:
        self.OPENAI_API_KEY = self.load_api_key()
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
        # self.llm = Replicate(
        #     model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        #     model_kwargs={"temperature": 0.4, "top_p": 1},
        # )

        # Prompt and method for converting Document -> str.
        self.document_prompt = PromptTemplate.from_template("{page_content}")
        self.partial_format_document = partial(
            format_document, prompt=self.document_prompt
        )

        self.collapse_chain = (
            {"context": self.format_docs}
            | PromptTemplate.from_template("Collapse this content:\n\n{context}")
            | self.llm
            | StrOutputParser()
        )

    def load_api_key(self):
        config_path = os.path.expanduser("~/.yt2brief/config.yaml")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path} \nPlease run `yt2brief-setup` to configure the API keys.")

        with open(config_path, "r") as config_file:
            api_keys = yaml.safe_load(config_file)

        return api_keys["OPENAI_API_KEY"]

    async def get_transcript(self, url):
        transcribe = Transcribe(url)

        transcript_file = transcribe.transcribe()

        # with open(transcript_file, "r") as f:
        #     transcript = f.read()

        return transcript_file

    # The chain we'll repeatedly apply to collapse subsets of the documents
    # into a consolidate document until the total token size of our
    # documents is below some max size.
    def format_docs(self, docs):
        return "\n\n".join(self.partial_format_document(doc) for doc in docs)

    def get_num_tokens(self, docs):
        return (self.llm).get_num_tokens(self.format_docs(docs))

    def collapse(
        self,
        docs,
        config,
        token_max=4000,
    ):
        collapse_ct = 1
        while self.get_num_tokens(docs) > token_max:
            config["run_name"] = f"Collapse {collapse_ct}"
            invoke = partial(self.collapse_chain.invoke, config=config)
            split_docs = split_list_of_docs(docs, self.get_num_tokens, token_max)
            docs = [collapse_docs(_docs, invoke) for _docs in split_docs]
            collapse_ct += 1
        return docs

    async def summarize(self, url):
        transcript = await self.get_transcript(url)

        if transcript is None:
            return "Invalid URL"

        loader = TextLoader(transcript)
        docs = loader.load()

        # print(docs)

        prompt_template = """Write a concise summary of the following youtube video transcript. Include all the things that is being told in the transcript:
        {context}


        Make the summary descriptive and concise. Consider all the points that are being told in the transcript.
        """

        # with open("config.json", "r") as config_file:
        #     config = json.load(config_file)

        # prompt_config = f"""
        # Use the following configutration to write the summary:

        # tone : {config["summary"]["tone"]},
        # use of bullet point : {config["summary"]["bullet-points"]["use"]},
        # average sentence length : {config["summary"]["bullet-points"][
        #     "average-sentence-length"
        # ]},
        # use of paragraphs : {config["summary"]["paragraphs"]["use"]},
        # average paragraph length : {config["summary"]["paragraphs"][
        #     "average-paragraph-length"
        # ]},
        # use of emojis : {config["summary"]["emojis"]},
        # markdown language use: {config["summary"]["markdown"]},
        # """

        # foo = prompt_template + prompt_config
        # print(foo)

        prompt = PromptTemplate.from_template(prompt_template)

        # The chain we'll apply to each individual document.
        # Returns a summary of the document.
        map_chain = (
            {
                "context": self.partial_format_document,
            }
            | prompt
            | self.llm
            | StrOutputParser()
        )

        # A wrapper chain to keep the original Document metadata
        map_as_doc_chain = (
            RunnableParallel({"doc": RunnablePassthrough(), "content": map_chain})
            | (
                lambda x: Document(
                    page_content=x["content"], metadata=x["doc"].metadata
                )
            )
        ).with_config(run_name="Summarize (return doc)")

        # The chain we'll use to combine our individual document summaries
        # (or summaries over subset of documents if we had to collapse the map results)
        # into a final summary.

        reduce_chain = (
            {"context": self.format_docs}
            | PromptTemplate.from_template("Combine these summaries:\n\n{context}")
            | self.llm
            | StrOutputParser()
        ).with_config(run_name="Reduce")

        # The final full chain
        map_reduce = (
            map_as_doc_chain.map() | self.collapse | reduce_chain
        ).with_config(run_name="Map reduce")

        # print(config["summary"]["paragraphs"]["average-paragraph-length"])

        format = Reformat(
            map_reduce.invoke(
                docs,
                config={
                    "max_concurrency": 5,
                },
            )
        )

        return await format.reformat()
