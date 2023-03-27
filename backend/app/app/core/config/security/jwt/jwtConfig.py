import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from jose import jwt
from datetime import timedelta
from app.core.config.settings.settingsConfiguration import settings
from typing import Optional, List, Dict, Any


class JwtConfig:
    def __init__(self):
        self.algorithm = "HS256"
        self.secret_key = ""

    def generate_token(self, sub: str) -> str:
        pass

    def decode_token(self, data: dict) -> Any:
        pass

    def get_algorithm(self):
        return self.algorithm

    def get_secret_key(self):
        return self.secret_key

