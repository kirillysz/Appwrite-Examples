from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.env")

class Config:
    ENDPOINT = getenv("ENDPOINT")
    PROJECT_ID = getenv("PROJECT_ID")
    API_KEY = getenv("API_KEY")
