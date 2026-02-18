import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.environ.get("PROVIDER")
MODEL = os.environ.get("MODEL")
API_KEY = os.environ.get("API_KEY")

pass