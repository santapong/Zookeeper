import os, sys
from dotenv import load_dotenv
sys.path.append(os.path.join(os.getcwd(),'prototype'))
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, create_session
