from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser

import os
from dotenv import load_dotenv
import json
import yaml

load_dotenv()


class Reformat:
    def __init__(self, summary) -> None:
        self.summary = summary
        self.OPENAI_API_KEY = self.load_api_key()
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k", api_key=self.OPENAI_API_KEY)
        self.prompt = self.template()

    def load_api_key(self):
        config_path = os.path.expanduser("~/.yt2brief/config.yaml")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path} \nPlease run `yt2brief-setup` to configure the API keys.")

        with open(config_path, "r") as config_file:
            api_keys = yaml.safe_load(config_file)

        return api_keys["OPENAI_API_KEY"]
    
    def template(self) -> str:
        prompt_tempate = """
        The below is a summary of the video. Please reformat it to make it more readable according to the following configuration:
        {summary}


        The configuration should as follows:
        tone: {tone}
        use of bullet points: {use_of_bullet_points}
        average sentence length: {average_sentence_length}
        use of paragraphs: {use_of_paragraphs}
        average paragraph length: {average_paragraph_length}
        use of emojis: {use_of_emojis}
        markdown language use: {markdown_language_use}

        """

        prompt = PromptTemplate(
            template=prompt_tempate,
            input_variables=[
                "summary",
                "tone",
                "use_of_bullet_points",
                "average_sentence_length",
                "use_of_paragraphs",
                "average_paragraph_length",
                "use_of_emojis",
                "markdown_language_use",
            ],
        )

        return prompt

    async def reformat(self):
        llm_chain = self.prompt | self.llm | StrOutputParser()

        # llm_chain.input_schema.schema()

        with open("config.json", "r") as f:
            config = json.load(f)

        return llm_chain.invoke(
            {
                "summary": self.summary,
                "tone": config["summary"]["tone"],
                "use_of_bullet_points": config["summary"]["bullet-points"]["use"],
                "average_sentence_length": config["summary"]["bullet-points"][
                    "average-sentence-length"
                ],
                "use_of_paragraphs": config["summary"]["paragraphs"]["use"],
                "average_paragraph_length": config["summary"]["paragraphs"][
                    "average-paragraph-length"
                ],
                "use_of_emojis": config["summary"]["emojis"],
                "markdown_language_use": config["summary"]["markdown"],
            }
        )
