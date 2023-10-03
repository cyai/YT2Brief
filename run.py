from yt2brief.summarize import Summarize


if __name__=="__main__":

    url = input("Enter the URL of the video: ")

    summarize = Summarize(url)

    print(summarize.summarize())