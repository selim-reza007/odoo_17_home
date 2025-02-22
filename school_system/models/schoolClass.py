from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = 'school.schoolclass'
    _description = 'school class module'

    name = fields.Char("Class name")
    capacity = fields.Integer("Max students")