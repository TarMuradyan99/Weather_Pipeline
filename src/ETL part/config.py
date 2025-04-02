from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.API_KEY = os.getenv("Api_key")
        self.PYTHON_PATH = os.getenv("python_path")
        self.PROJECT_PATH = os.getenv("python_project_path")
        self.DATA_BASE_PATH = os.getenv("DB_path")
        self.DEFAULT_CITY = ["yerevan","gyumri","vanadzor","spitka","sisian"]

