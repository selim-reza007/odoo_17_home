from odoo import api, models, fields

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital patient appointment"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    room = fields.Char("Bed no.")
    appointment_date = fields.Date(string="Appointment date", default=fields.Date.today())
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    state = fields.Selection([
        ('bed', 'Bed'),
        ('visited', 'Visited'),
        ('prescribed', 'Prescribed'),
        ('released', 'Released'),
        ('cancelled', 'Cancelled'),
    ], string='Appointment Status')
