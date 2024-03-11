import json


from application import db
from flask import Response, request, flash
from application.api.models.agenda import Agenda



def agenda_form():
    glpi = request.form.get('id')
    data = request.form.get('data')
    autor = request.form.get('autor')
    responsaveis = request.form.get('responsaveis')
    horario = request.form.get('horario')


    data = data.replace("/","-")


    nova_agenda = Agenda(data=data, id=glpi, autor=autor, responsavel=responsaveis, horario=horario)

    db.session.add(nova_agenda)
    db.session.commit()


    return True


def api_agenda_backend(data):
    agendas = Agenda.query.filter_by(data=data).all()


    api_data = [{'glpi': agenda.id,
                     'autor': agenda.autor,
                     'responsavel': agenda.responsavel,
                     'horario': agenda.horario,
                     'data': agenda.data} for agenda in agendas]
    
    response_data = {'agendas': api_data}

    
    json_response = json.dumps(response_data, ensure_ascii=False)
    response = Response(json_response, content_type='application/json; charset=utf-8')


    return response
