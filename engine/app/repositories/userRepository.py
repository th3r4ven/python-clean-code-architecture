from engine.app.repositories.models.user import UserModel
from engine.app.repositories.models import db


class UserRepository:

    def save(self, user):
        new_user = UserModel(username=user.username, email=user.email, password=user.password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_all(self):
        return UserModel.query.all()

    def get_by_id(self, user_id):
        return UserModel.query.get(user_id)

    def delete(self, user_id):
        user = UserModel.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
