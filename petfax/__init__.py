# imports
from flask import Flask
from flask_migrate import Migrate

# factory function
def create_app():
    app = Flask(__name__)

    #db config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:N_j02122016@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFACTIONS'] = False
    
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    @app.route('/')
    def index():
        return 'Hello, PetFax!'
    
    #register Blueprints
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)
    
    return app