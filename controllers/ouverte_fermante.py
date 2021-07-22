@auth.requires_login()
def ajout_ouverte_fermante():
    rows = db().select(db.ouverte_fermante.ALL)
    if len(rows):
        elt = rows[0]
        redirect(URL('modifier_ouverte_fermante', args=(elt.id)))
    else:
        form = SQLFORM(db.ouverte_fermante)
    if form.process().accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_ouverte_fermante')))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

@auth.requires_login()
def list_ouverte_fermante():
    rows = db().select(db.ouverte_fermante.ALL)
    return dict(rows=rows)

@auth.requires_login()
def supprimer_ouverte_fermante():
    db(db.ouverte_fermante.id ==  request.args(0)).delete()
        
    return dict(form=redirect(URL('list_ouverte_fermante')), message=T('Un enrégistrement d\'un ouverte/fermante a été supprimé'))

@auth.requires_login()
def modifier_ouverte_fermante():
    ouverte_fermante = db.ouverte_fermante(request.args(0)) or redirect(URL('error'))
    form = SQLFORM(db.ouverte_fermante, ouverte_fermante)
    form.process(detect_record_change=True)
    if form.record_changed:
        response.flash = 'form changed'
        return dict(form=redirect(URL('list_ouverte_fermante')))
    elif form.accepted:
        response.flash = 'form accepted'
        return dict(form=redirect(URL('list_ouverte_fermante')))
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, ouverte_fermante=ouverte_fermante)

def detail():
    ouverte_fermante = db.ouverte_fermante(request.args(0)) or redirect(URL('error'))

    return dict(ouverte_fermante=ouverte_fermante)