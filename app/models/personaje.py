class Personaje:
    def __init__(self,ID,name,status,species,type,origin,image,created,last,episodios):
        self.id=ID
        self.name=name
        self.status=status
        self.species=species
        self.type=type
        self.origin = origin
        self.image = image
        self.created = created
        self.last = last
        self.episodios = episodios

    def to_json(self):
      return {
          'id':self.id,
          'name':self.name,
          'status':self.status,
          'species':self.species,
          'type':self.type,
          'origin':self.origin,
          'image':self.image,
          'created':self.created,
          'last':self.last,
          'episodios':self.episodios}
