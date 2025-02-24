from odoo import api, fields, models

class InheritSaleOrder(models.Model):
    _inherit = "sale.order"

    country = fields.Char("Country")