from yt2brief.summarize import Summarize
from yt2brief.notion_integraion.create_page import Notion
import asyncio


async def main():
    url = input("Enter the URL of the video: ")
    isContinue = True
    while True:
        summarize = Summarize(url)

        summary = await summarize.summarize()
        # summary = """🎥 Video Summary: Embracing Aging and Defying Societal Norms 🎉 

        # 📝 The video transcript explores the cultural perception of aging and challenges the notion that 60 is the new 40.

        # The speaker, a geriatric nurse, advocates for embracing and celebrating one's age instead of trying to relive younger years.
        
        # 🌍 The concept of cultural lag is mentioned, highlighting the delay in societal attitudes towards aging compared to the rapid evolution of material culture. 
        
        # 🌟 The speaker encourages individuals to defy societal norms and stereotypes about aging, promoting innovation and creativity in the aging process. 
        
        # 💪 The importance of finding role models for aging and prioritizing physical and mental well-being is emphasized. 
        
        # ⏳ The potential for increased longevity is acknowledged, emphasizing the need to focus on quality of life rather than mere quantity. 
        
        # 🌈 The speaker suggests that cultivating wonder and discovering new passions can enhance the aging experience. 
        
        # 🤝 The significance of social connections and purpose in combating loneliness and maintaining good health is discussed. 
        
        # 📣 The transcript concludes with a call to change the narrative surrounding aging and to focus on the positive aspects of growing older. 
        
        # Let's celebrate the beauty of aging and rewrite the story! 🎉🌟💪🌈🤝📣"""

        # summary = "hello"

        # print(type(summary))

        usr_continue = input("Do you want to resummarize? (y/n): ")
        if usr_continue == "n":
            notion = Notion(str(summary), url)
            notion.create_page(str(summary))
            break


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
