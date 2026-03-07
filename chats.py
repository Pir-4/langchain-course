from langchain_ollama import ChatOllama, OllamaEmbeddings
from config import PROVIDER, MODEL, API_KEY, EMBED_MODEL


def chat_factory(
        provider=PROVIDER,
        model=MODEL,
        api_key=API_KEY,
        temperature:float = 0
):
    if provider =='ollama':
        return ChatOllama(
            model=model,
            temperature=temperature,
        )
    raise ValueError(f'Not support provider {provider}')

llm = chat_factory()
creative_llm = chat_factory(temperature=0.9)
embedding_llm = OllamaEmbeddings(model=EMBED_MODEL)
