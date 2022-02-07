from datetime import date, datetime
from odoo import api,fields,models
from dateutil.relativedelta import relativedelta

class property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "estate property offer"

    price = fields.Float()
    status = fields.Selection(selection=[("accepted","accepted"),("refused","Refused")],copy=False)
    property_id = fields.Many2one ('estate.property')
    partner_id = fields.Many2one ('res.partner')
    validity=fields.Integer(default=7)
    
    cust_id=fields.One2many("course.session")
