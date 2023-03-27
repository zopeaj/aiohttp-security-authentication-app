import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = sys.environ["FILE_PATH"]
sys.path.append(path)

from typing import Any
from app.db.base import Base
from sqlalchemy import Column, String, Integer, Sequence
from uuid import uuid4

class User(Base):
    id = Column(Integer, primary_key=True, Sequence("user_id_seq"), default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    password = Column(String, nullable=False)
    isAdmin = Column(Boolean, nullable=False)
    isActive = Column(Boolean, nullable=False)

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getEmail(self) -> str:
        return self.email

    def setEmail(self, email: str) -> None:
        self.email = email

    def getAge(self) -> str:
        return self.age

    def setAge(self, age: int) -> None:
        self.age = age

    def getGender(self) -> str:
        return self.gender

    def setGender(self, gender: str) -> None:
        self.gender = gender

    def password(self) -> str:
        return self.password

    def setPassword(self, password: str) -> None:
        self.password = password

    def getUsername(self) -> str:
        return self.email

    def getIsAdmin(self) -> bool:
        return self.isAdmin

    def setIsAdmin(self, isAdmin: bool) -> None:
        self.isAdmin = isAdmin

    def getIsActive(self) -> bool:
        return self.isActive

    def setIsActive(self, isActive: bool) -> None:
        this.isActive = isActive

    def isAccountNonExpired() -> bool:
        return True

    def isCredentialsNonLocked() -> bool:
        return True

    def isCredentialsNonExpired() -> bool:
        return True

    def isEnabled() -> bool:
        return True

    def getAuthories() -> Any:
        return None
