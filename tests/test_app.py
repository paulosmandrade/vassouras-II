from vassouras_ii.app import create_app, socketio


def test_socketio_connect():
    app = create_app()
    client = socketio.test_client(app)
    assert client.is_connected()
    client.disconnect()
