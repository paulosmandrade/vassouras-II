from datetime import datetime

import pytz
from flask_login import UserMixin
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

BRTZ = pytz.timezone('America/Sao_Paulo')


def current_time_brasilia():
    return datetime.now(BRTZ)


class Usuarios(Base, UserMixin):
    __tablename__ = 'cadastro_usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=current_time_brasilia)
    updated_at = Column(
        DateTime, default=current_time_brasilia, onupdate=current_time_brasilia
    )
    id_usuario = Column(Integer, index=True)
    username = Column(String(30), unique=True)
    email = Column(String(30), unique=True)
    password = Column(String(100))
    code = Column(String(6))
    status = Column(Boolean)

    def __repr__(self):
        return f'<Usuario {self.username}>'
