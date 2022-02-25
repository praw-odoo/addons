import string
from odoo import api, fields, models
from datetime import datetime, timedelta

class ResPartner(models.Model):
    _inherit="res.partner"

    days_to_deliver = fields.Integer(string="Days to Deliver")
    
class SaleOrder(models.Model):
    _inherit="sale.order"

    appointment_date = fields.Datetime(string="Appointment Date")
    zero_stock_approval = fields.Boolean(string="Zero Stock Approval")

    #if zero_stock_approval:


    # commitment_date = fields.Datetime(compute="_onchange_days")

    # @api.depends("appointment_date")
    # def _onchange_days(self):
    #     if self.appointment_date:
    #         self.commitment_date=self.appointment_date+timedelta(days=ResPartner.days_to_deliver)
    #         #self.commitment_date=self.appointment_date - self.partner_id.days_to_deliver.strftime("%Y%m%d")
