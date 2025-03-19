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
        ('prescribe', 'Prescribe'),
        ('released', 'Released'),
        ('cancelled', 'Cancelled'),
    ], string='Appointment Status')

    def state_bed(self):
        self.write({'state' : 'bed'})

    def state_visited(self):
        self.write({'state': 'visited'})

    def state_prescribe(self):
        self.write({'state': 'prescribe'})

    def state_released(self):
        self.write({'state': 'released'})

    def state_cancelled(self):
        self.write({'state': 'cancelled'})
