from engine.app.core.entities.user import User
from engine.app.services.password_hasher import PasswordHasher


class UserCRUDUseCase:

    def __init__(self, repository, pass_hasher: PasswordHasher):
        self.repository = repository
        self.pass_hasher = pass_hasher

    def create_user(self, username, email, password):
        user = User(username, email, password)
        user.validate_password()
        user.password = self.pass_hasher.hash_password(user.password)
        return self.repository.save(user)

    def get_all_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, user_id):
        return self.repository.get_by_id(user_id)

    def delete_user(self, user_id):
        return self.repository.delete(user_id)
