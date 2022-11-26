from flask import Flask
from flask_bootstrap import Bootstrap
from .routes.personajes import personajes_ruta


def create_app():

  app=Flask(__name__)
  app.register_blueprint(personajes_ruta)
  Bootstrap(app)
  
  return app