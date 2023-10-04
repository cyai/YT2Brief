from yt2brief.summarize import Summarize


if __name__ == "__main__":
    url = input("Enter the URL of the video: ")
    isContinue = True
    while isContinue:
        summarize = Summarize(url)

        print(summarize.summarize())

        isContinue = input("Do you want to resummarize? (y/n): ")
        if isContinue == "n":
            isContinue = False
            break
