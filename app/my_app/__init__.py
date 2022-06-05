import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from my_app import db
    db.init_app(app)

    from my_app import table
    app.register_blueprint(table.bp)

    #app.add_url_rule("/", endpoint="index")

    return app

