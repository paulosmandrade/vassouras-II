from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


# Criptografa a senha (Argon mais segura)
def get_password_hash(password: str):
    return pwd_context.hash(password=password)


# Verifica senha - Retorna Bool
def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)
