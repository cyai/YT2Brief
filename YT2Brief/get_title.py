from bs4 import BeautifulSoup
import requests
import json


def fetch_title(url):
    request = requests.get(url)
    text = BeautifulSoup(request.text, "html.parser")

    title = text.find("title").text
    # YouTube's title tag includes " - YouTube", so we remove it
    title = title.replace(" - YouTube", "")

    return title
