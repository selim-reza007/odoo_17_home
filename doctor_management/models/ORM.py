#Create method
from itertools import count

from odoo import fields

class Doctor(models.Model):
    _name = 'doctor.doctor'
    _description = 'Doctor class'

    name = fields.Char("Name")
    degree = fields.Char("Degree")
    days = fields.Many2many('hospital.days', string="Select days")
    fee = fields.Integer("Fee")

    self.env['doctor.doctor'].create({'name':'Shahin Alom', 'degree':'MBA'})
    self.env['doctor.doctor'].browse(5)
    self.env['doctor.doctor'].browse(5).write({'name':'Selim Khan', 'degree':'B.Sc'})
    self.env['doctor.doctor'].browse(5).unlink()
    self.env['doctor.doctor'].search([], limit=3, order='id desc')

    self.env['doctor.doctor'].search_count([('degree','=','B.Sc')], count=True)
    self.env['hospital.tag'].browse(99).get_metadata()[0].get('xmlid')
    self.env['doctor.doctor'].fields_get(['name','degree'],['type','string'])
