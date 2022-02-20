from odoo import models, api, fields

class travel(models.Model):
    _name="travel.travel"

    name=fields.Char()
    destination=fields.Char()
    start_date=fields.Date()
    end_date=fields.Date()
    