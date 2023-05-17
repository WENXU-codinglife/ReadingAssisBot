import os
from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage

from utils.utils import generate_directory_structure
# Load environment variables from .env file
load_dotenv() 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
STORAGE = './storage'

# scan the data dir
dir_structure = generate_directory_structure(STORAGE)
# remove the empty dir
dir_structure = [x for x in dir_structure if len(x) > 1]

index_dic = {}

for course in dir_structure:
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=f"{STORAGE}/{course[0]}")
    # load index
    index = load_index_from_storage(storage_context)
    # add to index dictionary
    index_dic[f"{course[0]}"] = index



def qna(course, query):
    index = index_dic[course]
    query_engine = index.as_query_engine()
    return query_engine.query(query)
