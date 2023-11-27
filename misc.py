from dataclasses import dataclass
import os
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Set up database connection
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


@dataclass()
class AvatarexSettings:
    knowledge_link: str
    context: str
    api_token: str
    error_message: str


def read_database():
    pass


def get_execution_function():
    pass


def read_avatarex_settings() -> AvatarexSettings:
    avatarexsettings = Table(
        'home_avatarexsettings', metadata,
        Column('id', Integer, primary_key=True),
        Column('knowledge_link', String),
        Column('context', String),
        Column('api_token', String),
        Column('error_message', String),
    )

    # Read data from the table where id = 2
    result = session.query(avatarexsettings).filter(avatarexsettings.c.id == 2).first()
    return AvatarexSettings(
        knowledge_link=result.knowledge_link,
        context=result.context,
        api_token=result.api_token,
        error_message=result.error_message
    )


