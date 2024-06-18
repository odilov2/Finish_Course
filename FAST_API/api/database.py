from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine('postgresql://postgres:7983@localhost/modul_8', echo=True)
Base = declarative_base()
session = sessionmaker()