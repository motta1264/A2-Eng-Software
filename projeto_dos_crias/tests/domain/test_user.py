from domain.user import User

def test_user_creation():
    user = User(id=1, name="Alice", email="alice@email.com", password_hashed="hashed_pw", faculdade="UF", cursos="Engenharia")
    assert user.id == 1
    assert user.name == "Alice"
    assert user.email == "alice@email.com"
    assert user.password_hashed == "hashed_pw"
    assert user.faculdade == "UF"
    assert user.cursos == "Engenharia"