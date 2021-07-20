from sqlalchemy import create_engine
import os
from .. import models
engine = create_engine(os.environ['DB_CONNECT_L'])

# models.Base.metadata.create_all(bind=engine)
