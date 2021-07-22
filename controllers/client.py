@auth.requires_login()
def ajout_client():
    form = SQLFORM(db.client)

    mode_reservation = False
    if request.vars.affiche_id:
        mode_reservation = True
        session.affiche_id = request.vars.affiche_id
        my_extra_element = TR(LABEL('Nombre de plat à réserver : '),
                      INPUT(_name='nombre_place', _type='number', _required=True, _min=1, _class="integer form-control"))
        form[0].insert(-1, my_extra_element)

    nom = request.vars.nom
    prenom = request.vars.prenom
    message=T('')


    if form.process().accepted:
        response.flash = 'form accepted'
        for row in db().select(db.client.ALL):
            count = 0
            for _row in db().select(db.client.ALL):
                if row.nom == _row.nom and row.prenom == _row.prenom:
                    count += 1
                    if count >= 2:
                        try:
                            db(db.client.id ==  _row.id).delete()
                        except Exception as e:
                            print("Une erreur s'est produit")
            count = 0
        person = db.client(nom=nom, prenom=prenom)
        if session.affiche_id:
            
            
            place = db.reservation.insert(plat_id=session.affiche_id, client_id=person.id, nombre_plat=request.vars.nombre_place)
            
            session.affiche_id = 0
            message=T('Film réservé')
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, message=message, mode_reservation=mode_reservation)


@auth.requires_login()
def list_client():
    rows = db().select(db.client.ALL)
    return dict(rows=rows)

@auth.requires_login()
def supprimer_client():
    db(db.client.id ==  request.args(0)).delete()
        
    return dict(form=redirect(URL('list_client')), message=T('Un enrégistrement d\'un client a été supprimé'))

@auth.requires_login()
def modifier_client():
    client = db.client(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.client, client)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('list_client')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_client')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, client=client)

def detail():
    client = db.client(request.args(0)) or redirect(URL('error'))

    return dict(client=client)