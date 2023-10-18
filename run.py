from YT2Brief.summarize import Summarize


def main():
    while True:
        video_url = input("Enter the URL of the video: ")
        summarizer = Summarize(video_url)
        summary = summarizer.summarize()

        print(summary)

        is_continue = input("Do you want to resummarize? (y/n): ").strip().lower()
        if is_continue != "y":
            break


if __name__ == "__main__":
    main()
