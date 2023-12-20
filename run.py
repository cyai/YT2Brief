from yt2brief.summarize import Summarize
from yt2brief.notion_integraion.create_page import Notion
import asyncio


def main():
    while True:
        video_url = input("Enter the URL of the video: ")
        summarizer = Summarize(video_url)
        summary = summarizer.summarize()


async def main():
    url = input("Enter the URL of the video: ")

    while True:
        summarize = Summarize()

        summary = await summarize.summarize(url)

        while summary == "Invalid URL":
            print("Invalid URL")
            url = input("Enter the URL of the video: ")
            summary = await summarize.summarize(url)

        print(f"\n\n{summary}\n\n")

        usr_continue = input("Do you want to resummarize? (y/n): ")
        if usr_continue == "n":
            notion = Notion(str(summary), url)
            notion.create_page()
            break


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
