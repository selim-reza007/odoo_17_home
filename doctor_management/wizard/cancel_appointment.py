from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

from odoo import api, fields, models, _

class CancelWizard(models.TransientModel):
    _name = "hospital.cancel.appointment.wizard"
    _description = "hospital cancel appointment wizard"

    ref = fields.Many2one('hospital.appointment', string="ref no.", domain=[('state','=','bed')])
    patient_id = fields.Many2one(related='ref.patient_id', string="Patient")
    cancel_date = fields.Date(string="Date", default=fields.Date.today())
    reason = fields.Char(string="Reason")

    def confirm_action(self):
        cancel_days = self.env['ir.config_parameter'].get_param('doctor_management.cancel_days')
        allowed_date = self.ref.appointment_date - relativedelta(days=int(cancel_days))
        if allowed_date < fields.date.today():
            raise ValidationError(_("This appointment can't be cancelled!"))
        self.ref.state = 'cancelled'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def cancel_action(self):
        return
