from transcribe import Transcribe


from langchain import PromptTemplate, LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import StuffDocumentsChain


import os
from dotenv import load_dotenv

load_dotenv()


class Summarize:
    def __init__(self, url) -> None:
        self.url = url
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")

    def get_transcript(self):
        transcribe = Transcribe(self.url)

        return transcribe.transcribe()

    def summarize(self):
        transcript = self.get_transcript()
        loader = TextLoader(transcript)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        all_splits = text_splitter.split_documents(docs)

        prompt_template = """Write a summary of the following youtube video transcript:
        {text}


        Keep the paragraphs shorter.
        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        stuff_chain = StuffDocumentsChain(
            llm_chain=llm_chain, document_variable_name="text"
        )

        return stuff_chain.run(all_splits)
