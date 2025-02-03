from engine.app.core.presenters.user.userPresenter import UserPresenter
from engine.app.core.usecases.user.crud_usecase import UserCRUDUseCase
from engine.app.repositories.userRepository import UserRepository
from engine.app.services.password_hasher import PasswordHasher

class UserController:
    def __init__(self):
        self.user_repository = UserRepository()
        self.pass_hasher = PasswordHasher()
        self.presenter = UserPresenter()
        self.user_use_case = UserCRUDUseCase(self.user_repository, self.pass_hasher)


    def create_user(self, data):
        user = self.user_use_case.create_user(data['username'], data['email'], data['password'])
        return self.presenter.present(user)

    def get_user_by_id(self, user_id):
        user = self.user_use_case.get_user_by_id(user_id)
        return self.presenter.present(user)

    def get_all_users(self):
        users = self.user_use_case.get_all_users()
        return self.presenter.present(users)

    def delete_user(self, user_id):
        user = self.user_use_case.delete_user(user_id)
        return self.presenter.present(user)

