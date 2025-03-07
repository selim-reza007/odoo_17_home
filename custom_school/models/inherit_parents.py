from odoo import api, fields, models

class InheritParents(models.Model):
    _inherit = 'school.parents'

    mobile = fields.Char("Mobile no.")