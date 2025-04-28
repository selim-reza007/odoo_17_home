from odoo import api, fields, models

class InheritSaleOrder(models.Model):
    _inherit = "sale.order"

    country = fields.Char("Country")

    def _prepare_invoice(self):
        values = super(InheritSaleOrder, self)._prepare_invoice()
        values['country'] = self.country
        return values


class InheritSaleOrderLine(models.Model):
    _inherit = "sale.order.option"

    country = fields.Char("Country")