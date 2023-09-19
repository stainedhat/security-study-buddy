import os
import databases
from sqlalchemy import MetaData, Table, Column, ForeignKey, create_engine
from sqlalchemy import Integer, String

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

DATABASE_URL = "sqlite:///test.db"
database = databases.Database(DATABASE_URL)

metadata = MetaData()

questions = Table(
    "questions",
    metadata,
    Column("question_id", Integer, primary_key=True),
    Column("question", String),
    Column("answer", String),
    Column("category", String),
)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
