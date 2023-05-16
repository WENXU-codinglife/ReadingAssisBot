import os
from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage
# Load environment variables from .env file
load_dotenv() 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir='./storage')
# load index
index = load_index_from_storage(storage_context)

def qna(query):
    query_engine = index.as_query_engine()
    return query_engine.query(query)
