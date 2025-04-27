from odoo import api, models, fields

class Days(models.Model):
    _name = "hospital.days"
    _description = "Available days"

    name = fields.Char("Day name", trim=False)
    color = fields.Integer('Color Index')