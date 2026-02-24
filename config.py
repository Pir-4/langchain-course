import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.environ.get("PROVIDER")
MODEL = os.environ.get("MODEL")
API_KEY = os.environ.get("API_KEY")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")

# below should not be changed
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://eu.api.smith.langchain.com"
# you can change this as preferred
os.environ["LANGCHAIN_PROJECT"] = "langchain-course-langsmith"
