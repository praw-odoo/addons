from odoo import api,fields,models

class intern(models.Model):
    _name="intern.intern"
    _description="Test Model"

    name = fields.Char(required=True)
    position = fields.Char()
    college = fields.Char(required=True)
    stipend = fields.Integer()
    date_join = fields.Date()
    date_comp = fields.Date()
    