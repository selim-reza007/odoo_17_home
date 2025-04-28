from odoo import api, fields, models

class InheritAccountMove(models.Model):
    _inherit = "account.move"

    country = fields.Char("Country")
