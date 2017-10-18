from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

#initializing flask extension
bootstrap =Bootstrap()


def create_app(config_name):
  
  app=Flask(__name__)

  #creating the app configurations
  app.config.from_object(config_options[config_name])

  #initializing bootstrap
  bootstrap.init_app(app)


  #we will add the views and the forms 
  from .main import main as main_blueprint 
  app.register_blueprint(main_blueprint)

  from .request import config_request
  config_request(app)

  return app


# from app import views
