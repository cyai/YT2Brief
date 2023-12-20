from yt2brief.utils.get_title import get_title
import requests
import json
import dotenv
import os

dotenv.load_dotenv()


class Notion:
    def __init__(self, content, url) -> None:
        self.content = str(content)
        self.url = "https://api.notion.com/v1/pages"
        self.title = get_title(url)
        self.database_id = os.getenv("NOTION_DATABASE_ID")
        self.notion_api_key = os.getenv("NOTION_API_KEY")

    def create_page(self):
        # print(type(content))

        payload = {
            "parent": {"database_id": f"{self.database_id}"},
            "icon": {"emoji": "✨"},
            "cover": {"external": {"url": f"{self.url}"}},
            "properties": {"Name": {"title": [{"text": {"content": f"{self.title}"}}]}},
            "children": [
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [
                            {"type": "text", "text": {"content": f"{self.title}"}}
                        ]
                    },
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": self.content,
                                },
                            }
                        ]
                    },
                },
            ],
        }

        # print(payload)

        # payload = json.dumps(payload)
        response = requests.post(
            self.url,
            headers={
                "Authorization": f"Bearer {self.notion_api_key}",
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28",
            },
            json=payload,
        )

        if response.status_code == 200:
            print("Success! ✨")

        else:
            print(f"Error: {response.status_code} {response.reason}")


# response = requests.post(
#     self.url,
#     headers={
#         "Authorization": f"Bearer {os.getenv('NOTION_API_KEY')}",
#         "Notion-Version": "2022-06-28",
#         "Content-Type": "application/json",
#     },
#     json={
#         "cover": {
#             "type": "external",
#             "external": {
#                 "url": "https://images.unsplash.com/photo-1701122623529-57a0c47e4e0e?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#             },
#         },
#         "icon": {"type": "emoji", "emoji": "💡"},
#         "parent": {
#             "type": "database_id",
#             "database_id": f"{self.database_id}",
#         },
#         "properties": {
#             "Name": {"title": [{"text": {"content": f"{self.title}"}}]},
#             "Description": {
#                 "rich_text": [{"text": {"content": f"{self.title}"}}]
#             },
#         },
#         "children": [
#             {
#                 "object": "block",
#                 "heading_2": {"rich_text": [{"text": {"content": "Summary!"}}]},
#             },
#             {
#                 "object": "block",
#                 "bulleted_list_item": {
#                     "rich_text": [
#                         {
#                             "text": {
#                                 "content": f"{self.content}",
#                             },
#                         }
#                     ],
#                     "color": "default",
#                 },
#             },
#         ],
#     },
# )
