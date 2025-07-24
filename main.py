from flask import Flask
from config import Config
from models import db


# aplicando configurações
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# blueprints
from routes.home import home_route
from routes.form import form_route

app.register_blueprint(home_route)
app.register_blueprint(form_route, url_prefix='/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)