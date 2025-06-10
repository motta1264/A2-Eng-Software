from domain.group import Group


def test_group_creation():
    group = Group(
        id=1,
        nome="Grupo A",
        descricao="descricao",
        materia="matematica",
        estilo="virtual",
        administrador_id=1,
    )
    assert group.id == 1
    assert group.nome == "Grupo A"
    assert group.descricao == "descricao"
    assert group.materia == "matematica"
    assert group.estilo == "virtual"
    assert group.administrador_id == 1
