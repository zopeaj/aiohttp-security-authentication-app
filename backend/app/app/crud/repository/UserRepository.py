import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import Depends
from app.db.get_db import get_db

class UserRepository:
    def __init__(self):
        self.db = Depends(get_db)

    def save(self, user):
        self.db.add(user)
        self.db.commit()
        self.refresh(user)
        return user

    def update(self, data, id):
        user = self.db.query(User)
               .where(User.getId(), id)
               .first()
        if user is not None:
            user.update(**data)
            return user
        return None


    def delete(self, id):
        user = self.db.query(User).where(User.getId(), id).first()
        if user is not None:
            self.db.delete(user)
            self.db.commit()
        return None

    def getByUsername(self, username):
        user = self.db.query(User).where(User.getUsername(), username).first()
        return user


userRepository = UserRepository()
