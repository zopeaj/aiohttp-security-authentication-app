import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from app.models.user import User
from app.core.business.abstracts.UserService import UserService
from app.core.business.concretes.EmailSenderService import EmailSenderService
from app.core.config.security.jwt.jwtConfig import JwtConfig
from app.core.config.security.passwordConfiguration import PasswordConfiguration
from app.schemas.userSchema import UserDTO



class AuthManager:
    def __init__(self, userService, emailSenderService, jwtConfig, passwordConfiguration):
        self.userService = userService
        self.emailSenderService = emailSenderService
        self.jwtConfig = jwtConfigq
        self.passwordConfiguration = passwordConfiguration

    def setAuthentication(username: str, password: str) -> User:
        pass

    def register(userDTO: UserDTO) -> Result:
        pass

    def authenticate(username: str, password: str) -> None:
        pass

    def confirmUser(username: str) -> Result:
        pass

authManager = AuthManager(UserService(), EmailSenderService(), JwtConfig(), PasswordConfiguration())
