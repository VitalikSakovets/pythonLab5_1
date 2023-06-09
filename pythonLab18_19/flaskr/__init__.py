import os
from flask import Flask

def create_app(test_config=None):# створення і задання конфігурацій застосунку
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # завантаження конфігурації екземпляра, якщо вона існує, # і якщо не виконується тестування
        app.config.from_pyfile('config.py', silent=True)
    else:
        # якщо передано конфігурації для тестування, то завантажити її
        app.config.from_mapping(test_config)
        # створення дерикторії instance, якщо її не існує
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # проста сторінка за маршрутом hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    return app