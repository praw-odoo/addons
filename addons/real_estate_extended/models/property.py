from odoo import api,fields,models

class property(models.Model):
    _inherit="estate.property"

    home_city=fields.Char()

class stateproperty(models.Model):
    _name="state.property"
    _inherit="estate.property"

    home_state=fields.Char()

class specialoffer(models.Model):
    _name="special.offer"
    _inherits={"estate.property":"property_id"}

    property_id = fields.Many2one ('estate.property')
    special_price=fields.Float()