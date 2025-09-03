from sqlalchemy import and_, select

from vassouras_ii.database import get_session
from vassouras_ii.models import Usuarios
from vassouras_ii.security import get_password_hash, verify_password
from vassouras_ii.settings import Settings
from vassouras_ii.utilitarios import consultar_codigo_usuario


def verifica_acesso(dados):
    with next(get_session()) as session:
        user = session.scalar(
            select(Usuarios).where(
                and_(Usuarios.email == dados['email'], Usuarios.status)
            )
        )
        if not user:
            return False, None

        if verify_password(dados['password'], user.password):
            return True, user

        return False, None


def verifica_cadastro_adm():
    with next(get_session()) as session:
        user_admin = session.scalar(
            select(Usuarios).where(Usuarios.email == Settings().EMAIL)
        )
        password = Settings().PASSWORD

        if not user_admin:
            user = Usuarios(
                id_usuario=1,
                username=Settings().USERNAME,
                email=Settings().EMAIL,
                password=get_password_hash(password),
                code=consultar_codigo_usuario(),
                status=True,
            )
            session.add(user)
            session.commit()
