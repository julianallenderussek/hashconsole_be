from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.db_credentials import username, password, database, url, port

# Define your database connection string
DATABASE_URL = f'mysql+pymysql://{username}:{password}@{url}:{port}/{database}'

# Create an engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()