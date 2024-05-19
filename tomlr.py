import toml

def read_toml():
    with open("cfg.toml", 'r', encoding='utf-8') as f:
        return toml.load(f)


toml_data = read_toml()

PROJECT_NAME = toml_data['project']['name']
PROJECT_VERSION = toml_data['project']['version']
PROJECT_DESCRIPTION = toml_data['project']['description']
PROJECT_AUTHOR = toml_data['project']['author']
PROJECT_AUTHOR_EMAIL = toml_data['project']['email']
PROJECT_URL = toml_data['project']['url']
NEWS=toml_data['new']['what']
