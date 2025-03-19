from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'Doctor class'

    name = fields.Char("Name")
    degree = fields.Char("Degree")
    days = fields.Many2many('hospital.days', string="Select days")
    fee = fields.Integer("Fee")