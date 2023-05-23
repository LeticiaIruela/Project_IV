from dotenv import load_dotenv
import sqlalchemy as alch
import os
def connection_sql (password,dbName):
    load_dotenv()
    password=os.getenv("password")
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine