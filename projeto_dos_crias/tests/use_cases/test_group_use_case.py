import pytest
from use_cases.group_use_case import GroupUseCase
from domain.group import Group

class FakeGroupRepository:
    def __init__(self):
        self.groups = []
        self.counter = 1
        self.participants = {}

    def add(self, group):
        group.id = self.counter
        self.counter += 1
        self.groups.append(group)
        self.participants[group.id] = set([group.administrador_id])
        return group

    def find_by_id(self, group_id):
        for g in self.groups:
            if g.id == group_id:
                return g
        return None

    def find_by_admin(self, admin_id):
        return [g for g in self.groups if g.administrador_id == admin_id]

    def find_participating_but_not_admin(self, user_id):
        return [g for g in self.groups if user_id in self.participants.get(g.id, set()) and g.administrador_id != user_id]

    def add_participant(self, grupo_id, user_id):
        self.participants.setdefault(grupo_id, set()).add(user_id)

    def user_participates(self, grupo_id, user_id):
        return user_id in self.participants.get(grupo_id, set())

def test_create_group():
    repo = FakeGroupRepository()
    use_case = GroupUseCase(repo)

    group = use_case.create("Grupo A", "descricao", "matematica", "virtual", admin_id=1)

    assert group.nome == "Grupo A"
    assert group.estilo == "virtual"
    assert group.administrador_id == 1

def test_participation_logic():
    repo = FakeGroupRepository()
    use_case = GroupUseCase(repo)

    group = use_case.create("Grupo B", "desc", "fisica", "presencial", 1)
    use_case.enter_group(group.id, 2)

    assert use_case.user_is_participant(group.id, 2)
    assert not use_case.user_is_participant(group.id, 3)

    groups = use_case.get_participating_but_not_admin(2)
    assert group in groups