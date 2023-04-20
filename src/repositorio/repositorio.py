import os
from sqlalchemy import create_engine, text

url= os.getenv('DATABASE_URL')

db_conn = None

if(db_conn == None):
  engine = create_engine(url)
  db_conn = engine.connect()


