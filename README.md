# YT2Brief 📺📝

Hey there, welcome to YT2Brief – where I make watching YouTube videos a breeze! This is just a fun little project I put together to help you turn those lengthy videos into quick, easy-to-digest summaries.

**What's the deal?**

You know those times when you want to catch up on some YouTube content, but you don't have hours to spare? That's where YT2Brief comes in. I use some fancy tech like Langchain and our private LLMs, along with OpenAI's LLMs, to transcribe and summarize videos for you.

### How do I use it?

-   **Clone the repo**
    ```bash
    git clone https://github.com/cyai/yt2Brief/
    ```
-   **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```
-   **Set environmental variables**
    -   Create a `.env` file in the root directory
    -   Add the following variables to the file
        ```bash
        OPENAI_API_KEY=<your_openai_api_key>
        NOTION_API_KEY=<notion_api_key>
        NOTION_DATABASE_ID=<notion_database_id>
        ```
        > Follow the instructions [here](https://developers.notion.com/docs/create-a-notion-integration) to get your notion api key and the database id

-   **Run the script**
    ```bash
    python main.py
    ```
-   **Enter the YouTube video URL and review your summary and enjoy 😊**



Just a heads up, this is a pet project, so don't expect perfection. But I promise it's a neat little tool to have fun with.

### Example:
For the video: https://www.youtube.com/watch?v=8Vt16kTtgm4

You get the result:

```text

🎥 Video Summary: Embracing Aging and Defying Societal Norms 🎉

📝 The video transcript explores the cultural perception of aging and challenges the notion that "60 is the new 40." The speaker, a geriatric nurse, advocates for embracing and celebrating one's age instead of trying to relive younger years.

🌍 The concept of cultural lag is mentioned, highlighting the delay in societal attitudes towards aging compared to the rapid evolution of material culture.

🌟 The speaker encourages individuals to defy societal norms and stereotypes about aging, promoting innovation and creativity in the aging process.

💪 The importance of finding role models for aging and prioritizing physical and mental well-being is emphasized.

⏳ The potential for increased longevity is acknowledged, emphasizing the need to focus on quality of life rather than mere quantity.

🌈 The speaker suggests that cultivating wonder and discovering new passions can enhance the aging experience.

🤝 The significance of social connections and purpose in combating loneliness and maintaining good health is discussed.

📣 The transcript concludes with a call to change the narrative surrounding aging and to focus on the positive aspects of growing older.

Let's celebrate the beauty of aging and rewrite the story! 💪
```

**TO DO:**

> Beautify Notion page
