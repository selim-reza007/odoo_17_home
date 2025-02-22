from odoo import models, fields, api

class Subjects(models.Model):
    _name = 'school.subjects'
    _description = 'school subject module'

    name = fields.Char("subject title")