import string
from odoo import api, fields, models
#from datetime import datetime, timedelta
import datetime

class ResPartner(models.Model):
    _inherit="res.partner"

    days_to_deliver = fields.Integer(string="Days to Deliver")
    
class SaleOrder(models.Model):
    _inherit="sale.order"

    appointment_date = fields.Datetime(string="Appointment Date")
    commitment_date = fields.Datetime(readonly=False,compute='commute_commitment_date')

    @api.depends("appointment_date")
    def commute_commitment_date(self):
        for record in self:
            if record.appointment_date and record.partner_id.days_to_deliver > 0 :
                record.commitment_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_to_deliver)
        