from http import HTTPStatus


def test_route_login_retorna_status_code_OK(client):
    """Testa rota '/' e '/login'"""
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert b'login' in response.data.lower()
