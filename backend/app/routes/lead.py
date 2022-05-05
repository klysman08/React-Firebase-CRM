# Lead routes
from app import db
from app import models
from app.serializers import LeadSchema

from flask import Blueprint, jsonify, request
from json import dumps as jsondump

lead = Blueprint('lead', __name__)

# Parameters: https://stackoverflow.com/questions/28229668/python-flask-how-to-get-route-id-from-url

@lead.route('/lead/', methods=['GET'])
def retrieve_all_leads():
    """Retrieve lead"""
    '''
    id  = request.args.get('id', None)
    empresa  = request.args.get('empresa', None)
    nome  = request.args.get('nome', None)

    if not id and not empresa and not nome:
        response = models.Lead.query.all()
    elif not empresa and not nome:
        response = models.Lead.query.filter_by(id=id).first()
    '''
    result = models.Lead.query.all()
    return LeadSchema(many=True).jsonify(result), 200

@lead.route('/lead/', methods=['POST'])
def create_lead():
    """Create post lead"""
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    tipo = request.form['tipo']
    etapa = request.form['etapa']
    data = request.form['data']
    expectativa = request.form['expectativa']

    lead_obj = models.Lead(
        nome = nome,
        email = email,
        telefone = telefone,
        tipo = tipo,
        etapa = etapa,
        data = data,
        expectativa = expectativa
    )

    db.session.add(lead_obj)
    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

@lead.route('/lead/update/', methods=['POST'])
def update_lead():
    """Update post lead"""
    id = request.form['id']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    tipo = request.form['tipo']
    etapa = request.form['etapa']
    data = request.form['data']
    expectativa = request.form['expectativa']

    lead_obj = models.Lead.query.filter_by(id=id).first()

    setattr(lead_obj, 'nome', nome)
    setattr(lead_obj, 'email', email)
    setattr(lead_obj, 'telefone', telefone)
    setattr(lead_obj, 'tipo', tipo)
    setattr(lead_obj, 'etapa', int(etapa))
    setattr(lead_obj, 'data', data)
    setattr(lead_obj, 'expectativa', expectativa)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

@lead.route('/lead/update_column/', methods=['POST'])
def update_lead_column():
    """Update post lead column"""
    id = request.form['id']
    key = request.form['key']
    value = request.form['value']

    lead_obj = models.Lead.query.filter_by(id=id).first()

    if key == "etapa":
        value = int(value)

    setattr(lead_obj, key, value)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code



@lead.route('/lead/<nome>', methods=['GET'])
def create_get_lead(nome):
    """Create get lead"""
    lead_obj = models.Lead( 
        nome=nome
    )

    db.session.add(lead_obj)
    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code

@lead.route('/lead/update/<id>/<key>/<value>', methods=['GET'])
def update_get_lead_column(id, key, value):
    """Update get lead column"""

    lead_obj = models.Lead.query.filter_by(id=id).first()

    if key == "etapa":
        value = int(value)

    setattr(lead_obj, key, value)

    db.session.commit()
    response = {
        'success': True,
    }
    status_code = 200
    return jsonify(response), status_code