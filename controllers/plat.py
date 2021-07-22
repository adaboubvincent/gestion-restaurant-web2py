@auth.requires_login()
def ajout_plat():
    form = SQLFORM(db.plat)
    if form.process().accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_plat')))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def list_plat():
    rows = db().select(db.plat.ALL)
    return dict(rows=rows)

@auth.requires_login()
def supprimer_plat():
    db(db.plat.id ==  request.args(0)).delete()
        
    return dict(form=redirect(URL('list_plat')), message=T('Un enrégistrement d\'un plat a été supprimé'))

@auth.requires_login()
def modifier_plat():
    plat = db.plat(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.plat, plat)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('list_plat')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_plat')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, plat=plat)

def detail():
    plat = db.plat(request.args(0)) or redirect(URL('error'))

    return dict(plat=plat)