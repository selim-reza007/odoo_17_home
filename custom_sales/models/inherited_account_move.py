from odoo import api, fields, models

class InheritSaleOrder(models.Model):
    _inherit = "account.move"

    country = fields.Char("Country")
