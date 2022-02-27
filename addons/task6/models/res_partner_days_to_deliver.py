from odoo import api, fields, models
#from datetime import datetime, timedelta


class ResPartner(models.Model):
    _inherit="res.partner"

    days_to_deliver = fields.Integer(string="Days to Deliver")
