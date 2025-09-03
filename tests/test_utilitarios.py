import re

from tests.conftest import UsuarioFactory  # ajuste o caminho se necessário
from vassouras_ii.utilitarios import (
    consultar_codigo_usuario,
    gerar_codigo_alfanumerico,
)


def test_gerar_codigo_alfanumerico_tamanho_string_maiuscula():
    codigo = gerar_codigo_alfanumerico()
    tamanho = 6
    # Verifica se retornou um string
    assert isinstance(codigo, str)
    # Verifica se o tamanho contém 6 digitos
    assert len(codigo) == tamanho
    # Verifica se tem letras em maiusculo
    assert bool(re.search(r'[A-Z]', codigo))


def test_consultar_codigo_usuario_com_banco(session):
    # Inserir um usuário existente
    usuario_existente = UsuarioFactory(code='ABC123')
    session.add(usuario_existente)
    session.commit()

    # Chamar a função que gera código único
    codigo = consultar_codigo_usuario()
    tamanho = 6
    # Verifica se não retorna o código existente
    assert codigo != 'ABC123'
    assert len(codigo) == tamanho
