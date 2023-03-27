from typing import Optional, Dict, List, Any
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: Any

class Token(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

    def getUsername(self):
        return self.username

class TokenPayload(BaseModel):
    sub: Optional[str] = None

    def getSub(self) -> Optional[str]:
        return self.sub
