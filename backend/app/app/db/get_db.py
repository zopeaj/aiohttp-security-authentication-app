import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.db.session import SessionLocal

def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

