import argparse
import asyncio
from yt2brief.summarize import Summarize
from yt2brief.notion_integraion.create_page import Notion


async def run():
    parser = argparse.ArgumentParser(
        description="Transcribe and summarize YouTube videos using Langchain with the power of LLMs."
    )
    parser.add_argument("url", help="The URL of the video to be downloaded.")

    args = parser.parse_args()

    summarize = Summarize()

    summary = await summarize.summarize(args.url)

    print(f"\n\n{summary}\n\n")

    notion = Notion(str(summary), args.url)
    notion.create_page()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()
