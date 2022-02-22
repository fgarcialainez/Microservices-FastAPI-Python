import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine)
from databases import Database

DEFAULT_DATABASE_URL = 'postgresql://postgres:postgres@localhost/cast-db'
DATABASE_URL = os.getenv('DATABASE_URL', DEFAULT_DATABASE_URL)

engine = create_engine(DATABASE_URL)
metadata = MetaData()

casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('nationality', String(20)),
)

database = Database(DATABASE_URL)