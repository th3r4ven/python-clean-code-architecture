
class UserPresenter:
    @staticmethod
    def present(user):
        """ Formata os dados do usuário na resposta """
        return {"data": {"id": user.id, "username": user.username, "email": user.email}}
