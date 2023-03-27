import os
import sys
from dotenv import load_dotenv
load_dotenv()

from app.db.base_class import Base
from app.models.user import User
