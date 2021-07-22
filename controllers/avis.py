@auth.requires_login()
def ajout_avis():
    ''' form = SQLFORM(db.avis)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form) '''
    form = SQLFORM(db.client)
    mode_avis = False
    if request.vars.affiche_id:
        mode_avis = True
        session.affiche_id = request.vars.affiche_id
        my_extra_element_objet = TR(LABEL('Objet d\'avis : '),
                      INPUT(_name='objet', _type='text', _required=True, _class="string form-control"))
        my_extra_element_description = TR(LABEL('Description d\'avis : ', _class="form-control-label col-sm-3"),
                      TEXTAREA(_name='description', _required=True, _min=1, _rows=10, _cols=40, _class="form-control text"))

        form[0].insert(-1, my_extra_element_objet)
        form[0].insert(-1, my_extra_element_description)

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
            
            
            db.avis.insert(plat_id=session.affiche_id, client_id=person.id, objet=request.vars.objet, description=request.vars.description)
            
            session.affiche_id = 0
            message=T('Avis enovyé')
    return dict(form=form, message=message, mode_avis=mode_avis)

@auth.requires_login()
def list_avis():
    rows = db().select(db.avis.ALL)
    return dict(rows=rows)

@auth.requires_login()
def supprimer_avis():
    db(db.avis.id ==  request.args(0)).delete()
        
    return dict(form=redirect(URL('list_avis')), message=T('Un enrégistrement d\'un avis a été supprimé'))

@auth.requires_login()
def modifier_avis():
    avis = db.avis(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.avis, avis)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('list_avis')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_avis')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, avis=avis)

def detail():
    avis = db.avis(request.args(0)) or redirect(URL('error'))

    return dict(avis=avis)