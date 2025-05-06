from odoo import api, fields, models

class SaleReport(models.Model):
    _inherit = "sale.report"

    country = fields.Char(string="Country", readonly=True)


    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['country'] = "s.country"
        return res