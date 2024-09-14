from flask import Flask
from config.config import Config
import pymongo 


client=pymongo.MongoClient("mongodb+srv://dharshan:WHJo0D8U5RwID1ph@cluster0.oewot.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.sample_mflix

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register routes
    from .routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app
