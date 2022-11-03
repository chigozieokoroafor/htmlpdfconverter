from flask import Flask
from flask_cors import CORS
from folder.routes.userRoutes import user

app = Flask(__name__)

app.config["SECRET_KEY"] = "thisisasupersecretkey"
CORS(app)

app.register_blueprint(user)