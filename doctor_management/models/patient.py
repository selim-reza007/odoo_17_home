from odoo import api, models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char("Name")
    age = fields.Integer("Age")
    mobile = fields.Char("Contact no.")