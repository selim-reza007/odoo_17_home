from odoo.exceptions import ValidationError
from odoo import api, models, fields, _

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital patient appointment"
    _rec_name = "ref"
    _order = "id desc"

    ref = fields.Char("Reference")
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    room = fields.Char("Bed no.")
    duration = fields.Float('Average duration')
    appointment_date = fields.Date(string="Appointment date")
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    state = fields.Selection([
        ('bed', 'Bed'),
        ('visited', 'Visited'),
        ('prescribe', 'Prescribe'),
        ('released', 'Released'),
        ('cancelled', 'Cancelled'),
    ], string='Appointment Status')
    operation = fields.Many2one("hospital.operation", string="Operation")
    progress = fields.Integer(string="Progress", compute="_compute_progress")

    @api.depends('progress')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'bed':
                rec.progress = 25
            elif rec.state == 'visited':
                rec.progress = 50
            elif rec.state == 'prescribe':
                rec.progress = 75
            elif rec.state == 'released':
                rec.progress = 100
            else:
                rec.progress = 0

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

    def unlink(self):
        for rec in self:
            if rec.state == "bed":
                raise ValidationError(_("Appointment can't be deleted when state is in bed state!"))
        return super(Appointment, self).unlink()

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('appointment.sequence.data')
        return super(Appointment, self).create(vals)

    def cancel_appointment(self):
        return self.env.ref('doctor_management.action_cancel_appointment_wizard').read()[0]
