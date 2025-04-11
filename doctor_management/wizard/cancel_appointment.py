from odoo import api, fields, models

class CancelWizard(models.TransientModel):
    _name = "hospital.cancel.appointment.wizard"
    _description = "hospital cancel appointment wizard"

    ref = fields.Many2one('hospital.appointment', string="ref no.", domain=[('state','=','bed')])
    patient_id = fields.Many2one(related='ref.patient_id', string="Patient")
    cancel_date = fields.Date(string="Date", default=fields.Date.today())
    reason = fields.Char(string="Reason")

    def confirm_action(self):
        self.ref.state = 'cancelled'
        return

    def cancel_action(self):
        return
