import click
import os
import yaml  

def get_api_key(api_key_name):
    return click.prompt(f"Enter your {api_key_name} API key", hide_input=True)

def setup():
    click.echo("Welcome to the API key setup!")

    api_keys = {}

    api_keys["OPENAI_API_KEY"] = get_api_key("OpenAI API Key")
    api_keys["NOTION_API_KEY"] = get_api_key("Notion API Key")
    api_keys["NOTION_DATABASE_ID"] = get_api_key("Notion Database ID")

    config_path = os.path.expanduser("~/.yt2brief/config.yaml")
    os.makedirs(os.path.dirname(config_path), exist_ok=True)

    with open(config_path, "w") as config_file:
        yaml.dump(api_keys, config_file)

    click.echo("API keys configured successfully!")

if __name__ == "__main__":
    setup()
