# from flask import Flask

# app = Flask(__name__)
# from app import views

# from flask import Flask
# from flask_mail import Mail
# from .config import Config
# app = Flask(__name__)
# app.config.from_object(Config)
# mail = Mail(app)
# from app import views

from flask import Flask
from flask_mail import Mail
from .config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)

# Initialize Flask-Mail
mail = Mail(app)

# Import views (routes)
from app import views
