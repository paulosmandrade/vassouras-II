from flask import Flask

from vassouras_ii.login import verifica_cadastro_adm
from vassouras_ii.routers import bp, login_manager
from vassouras_ii.settings import Settings
from vassouras_ii.socketio_config import socketio


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Settings().SECRET
    app.register_blueprint(bp)

    login_manager.init_app(app)
    login_manager.login_view = 'vassouras_ii.login'

    # Permite logar pelo Socketio
    socketio.init_app(
        app,
        manage_session=True,
        cors_allowed_origins=[
            'http://localhost:5000',
            'http://127.0.0.1:5000',
        ],
    )

    verifica_cadastro_adm()

    return app


if __name__ == '__main__':
    app = create_app()
    socketio.run(app, debug=True)
