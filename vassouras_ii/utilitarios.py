import random
import string

from sqlalchemy import select

from vassouras_ii.database import get_session
from vassouras_ii.models import Usuarios


def gerar_codigo_alfanumerico():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def consultar_codigo_usuario():
    while True:
        codigo = gerar_codigo_alfanumerico()

        with next(get_session()) as session:
            user = session.scalar(
                select(Usuarios).where(Usuarios.code == codigo)
            )

            if not user:
                return codigo
