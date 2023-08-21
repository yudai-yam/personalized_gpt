import mysql.connector
from mysql.connector import Error

class SQL_database:

    connection = None

    def create_server_connection(self, host_name, user_name, user_password):
        try:
            server_connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("MySQL server connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return server_connection
    

    def create_database(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()


    def create_db_connection(self, host_name, user_name, user_password, db_name):
        db_connection = None
        try:
            db_connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return db_connection



    def execute_query(self, connection, query):
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
            if not query.startswith("INSERT"):
                data = cursor.fetchall()
                return data
        except Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()

                

    def __init__(self):
        
        #server_connection = self.create_server_connection("localhost", "root", constants.SQL_PW)
        #create_database_query = "CREATE DATABASE hashmemo_help_query"
        #self.create_database(server_connection, create_database_query)

        #create_query_history_table = 
        """
           
            CREATE TABLE query_history (
            date DATE,
            query VARCHAR(1000)
            );

        """

        #db_connection = self.create_db_connection("localhost", "root", constants.SQL_PW, db) # Connect to the Database
        #self.execute_query(db_connection, create_query_history_table) # Execute our defined query

#SQL_database()
    