db = DAL('sqlite://gestion_restaurant.sqlite')
#db = DAL('mysql://adaboubvincent:PaUl@_ADA20100@adaboubvincent.mysql.pythonanywhere-services.com/gestioncinema')


OuverteFermante = db.define_table('ouverte_fermante',
    Field('heure_ouverte', 'time'),
    Field('heure_fermante', 'time'),
    format = "%(nom)s")

Categorie = db.define_table('categorie',
    Field('nom', 'string'),
    Field('description', 'text'),
    format = "%(nom)s")
Plat = db.define_table('plat',
    Field('image', 'upload'),
    Field('nom', 'string'),
    Field('prix', 'float'),
    Field('nombre', 'integer'),
    Field('categorie_id', 'reference categorie', label=T('Catégorie ')),
    Field('description', 'text'),
    format = "%(nom)s")
Client = db.define_table('client',
    Field('nom', 'string'),
    Field('prenom', 'string'),
    format = "%(nom)s %(prenom)s")
Reservation = db.define_table('reservation',
    Field('plat_id', 'reference plat', label=T('Plat à Réserver ')),
    Field('client_id', 'reference client', label=T('Client ')),
    Field('nombre_plat', 'integer'))

Avis = db.define_table('avis',
    Field('plat_id', 'reference plat', label=T('Plat à Réserver ')),
    Field('client_id', 'reference client', label=T('Client ')),
    Field('objet', 'string'),
    Field('description', 'text'))
