from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'Doctor class'

    name = fields.Char("Name")
    degree = fields.Char("Degree")
    days = fields.Char("Days")
    fee = fields.Integer("Fee")