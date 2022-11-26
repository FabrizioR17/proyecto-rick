from flask import Blueprint,render_template, request, flash
import requests
from app.models.personaje import Personaje
from app.db import db


personajes_ruta=Blueprint('personajes_ruta',__name__)

@personajes_ruta.route('/')
def index():
  personajes = db.personajes.find()
  return render_template('index.html', personajes = personajes)

@personajes_ruta.route('/insert')
def insertar():
    for i in range(1,21):
      url = 'https://rickandmortyapi.com/api/character?page=' + str(i)
      request_url = (requests.get(url)).json()['results']
      for info in request_url:
        _id = info['id']
        name = info['name']
        status = info['status']
        species = info['species']
        origin = info['origin']['name']
        type = info['type']
        image=info['image']
        created=info['created']
        last=info['location']['name']
        episodios=info['episode']
        personaje = Personaje(_id,name,status,species,type,origin,image,created,last,episodios)

        db.personajes.insert_one(personaje.to_json())

    return 'personaje insertado'

@personajes_ruta.route('/perfiles')
def perfiles():
  personajes = db.personajes.find()
  return render_template('perfiles.html', personajes = personajes)
