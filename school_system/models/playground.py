from odoo import api, models, fields

class Playground(models.Model):
    _name = 'playground'
    _description = 'Playground model'

    code = fields.Char("Code")
    result = fields.Char("Result")