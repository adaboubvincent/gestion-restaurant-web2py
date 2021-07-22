#@auth.requires_login()
def ajout_categorie():
    form = SQLFORM(db.categorie)
    if form.process().accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_categorie')))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

#@auth.requires_login()
def list_categorie():
    rows = db().select(db.categorie.ALL)
    return dict(rows=rows)

#@auth.requires_login()
def supprimer_categorie():
    db(db.categorie.id ==  request.args(0)).delete()
        
    return dict(form=redirect(URL('list_categorie')), message=T('Un enrégistrement d\'une categorie a été supprimée'))

#@auth.requires_login()
def modifier_categorie():
    categorie = db.categorie(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.categorie, categorie)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('list_categorie')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_categorie')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, categorie=categorie)

def detail():
    categorie = db.categorie(request.args(0)) or redirect(URL('error'))

    return dict(categorie=categorie)