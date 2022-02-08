from odoo import _, api, fields, models


class assignMaintainer(models.TransientModel):
    _name="assign.maintainer"

    maintainer_id=fields.Many2one("res.partner")

    def action_assign_maintainer(self):
        self.ensure_one()
        property=self.env['estate.property']
        ids=self.env.context.get('active_ids')
        propertys=property.browse(ids)
        propertys.write({'maintainer_id':self.maintainer_id})
        return True