import json

config_file = open("config.json", "r")
config = json.load(config_file)

tone = config["summary"]["tone"]
bullet_points_use = config["summary"]["bullet-points"]["use"]
average_sentence_length = config["summary"]["bullet-points"]["average-sentence-length"]
paragraphs_use = config["summary"]["paragraphs"]["use"]
average_paragraph_length = config["summary"]["paragraphs"]["average-paragraph-length"]
emojis_use = config["summary"]["emojis"]
markdown = config["summary"]["markdown"]


print(
    tone,
    bullet_points_use,
    average_sentence_length,
    paragraphs_use,
    average_paragraph_length,
    emojis_use,
    markdown,
)
