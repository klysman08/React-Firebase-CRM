from app import ma
from app.models import Lead

from marshmallow import fields, validates, ValidationError

class LeadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lead
        load_instance = True

    nome = fields.Str(required=True)
    email = fields.Str(required=False)
    telefone = fields.Str(required=False)
    tipo = fields.Str(required=False)
    etapa = fields.Str(required=False)
    data = fields.Str(required=False)
    expectativa = fields.Str(required=False)

    @validates('id')
    def validate_id(self, value):
        raise ValidationError('Never send the id')