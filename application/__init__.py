from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/semed'
print(f"Conectando ao banco de dados: {app.config['SQLALCHEMY_DATABASE_URI']}")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "KATOCHI"
app.config['PERMANENT_SESSION_LIFETIME'] = 20000000
app.config['STATIC_FOLDER'] = 'static'

app.config['UPLOAD_FOLDER'] = f"application/{app.config['STATIC_FOLDER']}/uploads"
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.session_protection = "strong"
login_manager.login_message = u"Bonvolu ensaluti por uzi tiun paĝon."
login_manager.login_message_category = "info"



from application import routes