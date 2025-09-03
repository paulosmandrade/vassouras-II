from vassouras_ii.security import get_password_hash, verify_password


def test_get_password_hash():
    password = '123Mudar'

    # Criptografa a senha
    hashed_password = get_password_hash(password)

    # Verifica se a senha criptografada é uma string
    assert isinstance(hashed_password, str)

    # Verifica se a senha criptografada não é igual à senha original
    assert hashed_password != password


def test_verify_password():
    password = '123Mudar'

    # Criptografa a senha
    hashed_password = get_password_hash(password)

    # Verifica se a senha corresponde ao hash
    assert verify_password(password, hashed_password)

    # Testa com uma senha incorreta
    wrong_password = 'senha_errada'
    assert not verify_password(wrong_password, hashed_password)
