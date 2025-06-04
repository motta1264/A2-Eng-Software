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
            administrador_id=admin_id
        )
        return self.repository.add(group)

    def get_group(self, group_id):
        return self.repository.find_by_id(group_id)
