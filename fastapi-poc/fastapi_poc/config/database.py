from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username='postgres',
    host='localhost',
    port=5437,
    database='dvdrental',
    password='123456' 
)

engine = create_engine(url)

Session = sessionmaker(bind = engine, autocommit=False, autoflush=False)

Base = declarative_base()