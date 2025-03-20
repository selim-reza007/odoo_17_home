from odoo import api, fields, models

class Tags(models.Model):
    _name = "hospital.tags"

    name = fields.Char("Tag name")

    _sql_constraints = [
        ('unique_tag_name', "unique(name)", "Tag name must be unique!")
    ]