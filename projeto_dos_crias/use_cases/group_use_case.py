from domain.group import Group


class GroupUseCase:
    def __init__(self, repository):
        self.repository = repository

    def create_group(self, nome, descricao, materia, estilo, admin_id):
        group = Group(
            id=None,
            nome=nome,
            descricao=descricao,
            materia=materia,
            estilo=estilo,
            administrador_id=admin_id,
        )
        return self.repository.add(group)

    def get_group(self, group_id):
        return self.repository.find_by_id(group_id)

    def list_by_user(self, user_id):
        return self.repository.find_by_user(user_id)

    def search_groups(self, termo, estilo=None):
        return self.repository.search(termo, estilo)

    def delete(self, grupo_id):
        return self.repository.delete(grupo_id)

    def find_by_id(self, grupo_id):
        return self.repository.find_by_id(grupo_id)

    def get_participating_but_not_admin(self, user_id):
        return self.repository.find_participating_but_not_admin(user_id)

    def enter_group(self, grupo_id, user_id):
        return self.repository.add_participant(grupo_id, user_id)

    def user_is_participant(self, grupo_id, user_id):
        return self.repository.user_participates(grupo_id, user_id)
