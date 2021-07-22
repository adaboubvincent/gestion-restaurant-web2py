@auth.requires_login()
def ajout_reservation():
    form = SQLFORM(db.reservation)
    if form.process().accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_reservation')))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def list_reservation():
    rows = db().select(db.reservation.ALL)
    return dict(rows=rows)

@auth.requires_login()
def supprimer_reservation():
    db(db.reservation.id ==  request.args(0)).delete()
        
    return dict(form=redirect(URL('list_reservation')), message=T('Un enrégistrement d\'une reservation a été supprimée'))

@auth.requires_login()
def modifier_reservation():
    reservation = db.reservation(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.reservation, reservation)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('list_reservation')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_reservation')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, reservation=reservation)

def detail():
    reservation = db.reservation(request.args(0)) or redirect(URL('error'))

    return dict(reservation=reservation)