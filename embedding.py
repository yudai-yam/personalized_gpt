import time
start_time = time.time()
import os
import constants

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI

#from langchain.chains import RetrievalQA
#from langchain.chains import VectorDBQA

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

stop_importing = time.time()
print(f"\nFunction took {stop_importing- start_time:.6f} seconds to import everything in embedding class.")


os.environ["OPENAI_API_KEY"] = constants.API_KEY

class Embedding:
    def __init__(self, query):

        loader = TextLoader('data.txt', "utf-8") # utf-8 is for 日本語

        index = VectorstoreIndexCreator(
            vectorstore_cls=Chroma, 
            embedding=OpenAIEmbeddings(),
            text_splitter=CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        ).from_loaders([loader])

        index.query(query, llm = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])) # the second argument is for understanding stuff irrelevant to the fed document
