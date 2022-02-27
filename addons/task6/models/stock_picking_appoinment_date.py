from odoo import api, fields, models

class StockMove(models.Model):
    _inherit="stock.picking"

    appointment_date = fields.Datetime(string="Appointment Date", compute="_compute_appointment_date", readonly=True)


    # @api.depends("appointment_date")
    # def commute_commitment_date(self):
    #     for record in self:
    #         if record.appointment_date and record.partner_id.days_to_deliver > 0 :
    #             record.commitment_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_to_deliver)
