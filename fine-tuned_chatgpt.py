from embedding import Embedding
from sql_database import SQL_database
import constants

""" query = sys.argv[1]
print(query) """


# connect to db
sql = SQL_database()
db_connection = sql.create_db_connection("localhost", "root", constants.SQL_PW, constants.DB_NAME) # Connect to the Database


while True:

    query = input("Ask anything (or 'exit' to quit): ")
    if query.lower() == 'exit':
        print("Exiting the program.")
        break  # Exit the loop
    else:
        print("You entered:", query)
        Embedding(query)
        print("\n")

       
        # store data
        data_to_be_stored = f"INSERT INTO {constants.TABLE_NAME} (date, query) VALUES (curdate(), '{query}');"

        
        sql.execute_query(db_connection, data_to_be_stored)





#break down of what vectorstoreindexcreator is doing    
""" data = loader.load()

#split
text_splitter = CharacterTextSplitter(chunk_size = 100, chunk_overlap = 0)
all_splits = text_splitter.split_documents(data)

#store
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

# generate
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
print(qa_chain({"query": query}) )
 """