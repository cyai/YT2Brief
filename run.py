from yt2brief.summarize import Summarize

import asyncio


async def main():
    url = input("Enter the URL of the video: ")
    isContinue = True
    while isContinue:
        summarize = Summarize(url)

        print(await summarize.summarize())

        isContinue = input("Do you want to resummarize? (y/n): ")
        if isContinue == "n":
            isContinue = False
            break


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
