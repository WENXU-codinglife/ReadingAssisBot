import os
from dotenv import load_dotenv

from llama_index import SimpleDirectoryReader, download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import LLMPredictor, GPTVectorStoreIndex, PromptHelper, ServiceContext
from langchain import OpenAI

from utils.utils import generate_directory_structure

load_dotenv() 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def indexGenerator(data_dir_path, persist_dir_path): 
    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
    loader = SimpleDirectoryReader(data_dir_path, recursive=True, exclude_hidden=True)
    documents = loader.load_data()

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

    max_input_size = 4096
    num_output = 256
    max_chunk_overlap = 20
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index = GPTVectorStoreIndex.from_documents(
        documents, service_context=service_context
    )

    index.storage_context.persist(persist_dir=persist_dir_path)

if __name__ == "__main__":
    # scan the data dir
    dir_structure = generate_directory_structure("./data")
    # remove the empty dir
    dir_structure = [x for x in dir_structure if len(x) > 1]

    for course in dir_structure:
        indexGenerator(data_dir_path=f"./data/{course[0]}", persist_dir_path=f"./storage/{course[0]}")