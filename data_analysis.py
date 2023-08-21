from sql_database import SQL_database
import constants   
import langchain 
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()

chat = ChatOpenAI(openai_api_key=f"{constants.API_KEY}", temperature=0)


# connect to db
sql = SQL_database()
db_connection = sql.create_db_connection("localhost", "root", constants.SQL_PW, constants.DB_NAME) # Connect to the Database



# fetch record
sql_query = f"SELECT query FROM {constants.TABLE_NAME};"

data = sql.execute_query(db_connection, sql_query)
print(data) 
data_list = [row[0] for row in data]

messages = [
    SystemMessage(content=f"This is the data that the user wants to deal with {data_list}"),
    HumanMessage(content="""
        Give me the topics of questions
        Similar questions should be gathered into one bigger topic.
        NEVER list original questions, just list TOPICS.
        The format is below.
        1. "TOPIC": "The number of occurrences"
        2. 
        3. 
        4.
        ....
""")]
print(chat(messages).content)
