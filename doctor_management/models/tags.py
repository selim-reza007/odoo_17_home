from odoo import api, fields, models

class Tags(models.Model):
    _name = "hospital.tags"

    name = fields.Char("Tag name")