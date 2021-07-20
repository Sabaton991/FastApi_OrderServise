from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
import logging

Base = declarative_base()
load_dotenv()


class DatabaseConnect:
    def __init__(self):
        self.db_connect = self._connect()
        self.db = self._get_db()

    def _connect(self):
        try:
            engine = create_engine(os.environ['DB_CONNECT_L'], convert_unicode=True)
            Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            logging.info('connected to db')
            return Session
        except Exception as e:
            logging.error(e)

    def _get_db(self):
        db = self.db_connect()
        try:
            yield db
        except Exception as e:
            logging.error(e)
        finally:
            db.close()
