from odoo import _, api, fields, models


class assignMaintainer(models.TransientModel):
    _name = "assign.maintainer"

    #maintainer_id = fields.Many2one("res.partner")
    #salesperson_id = fields.Many2one("res.user")
    buyer_id = fields.Many2one("res.partner")


    def action_assign_maintainer(self):
        self.ensure_one()
        propertyy=self.env['estate.property']
        ids=self.env.context.get('active_ids')
        propertys=propertyy.browse(ids)
        propertys.write({'buyer_id': self.buyer_id})
        return True