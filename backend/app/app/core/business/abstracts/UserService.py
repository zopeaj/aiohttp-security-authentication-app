from app.models.user import User
from app.crud.repository.UserRepository import userRepository

class UserService:
    def __init__(self, userRepository):
        self.userRepository = userRepository

    def create(self, user) -> User:
        user = self.userRepository.save(user)
        return user

    def update(self, update_data, id) -> User:
        return self.userRepository.update(user, id)

    def remove(self, id) -> None
        return self.userRepository.delete(id)

    def getUserByUsername(self, username) -> User:
        return self.userRepository.getByUsername(username)

userService = UserService(userRepository)
