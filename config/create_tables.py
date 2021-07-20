from sqlalchemy import create_engine
import os
from .. import db_models
engine = create_engine(os.environ['DB_CONNECT_L'])

# db_models.Base.metadata.create_all(bind=engine)
