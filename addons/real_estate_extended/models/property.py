from odoo import api,fields,models

class property(models.Model):
    _inherit="estate.property"

    home_city=fields.Char();

class stateproperty(models.Model):
    _name="state.property"
    _inherit="estate.property"

    home_state=fields.Char();