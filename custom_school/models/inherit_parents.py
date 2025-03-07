from odoo import api, fields, models

class InheritParents(models.Model):
    _inherit = 'school.parents'

    mobile = fields.Char("Mobile no.")
    ref = fields.Char("Reference")

    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('school.parent.sequence')
        return super(InheritParents, self).create(vals)