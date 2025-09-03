import factory
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from vassouras_ii.app import create_app
from vassouras_ii.models import Base, Usuarios


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture
def app(session):
    """Cria a aplicação de testes"""
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_ECHO': False,
    })
    app.session = session

    return app


@pytest.fixture
def client(app):
    """Fornece o test client Flask"""
    return app.test_client()


class UsuarioFactory(factory.Factory):
    class Meta:
        model = Usuarios

    id_usuario = factory.Sequence(lambda n: n + 1)
    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.username}@!#123Mudar')
    code = factory.Faker('bothify', text='######')
    status = True
