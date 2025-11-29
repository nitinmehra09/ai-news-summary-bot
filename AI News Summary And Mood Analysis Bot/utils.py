import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_env(key, default=None):
    return os.getenv(key, default)

def now_date_str():
    return datetime.now().strftime("%Y-%m-%d")
