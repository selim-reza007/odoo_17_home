from odoo import api, fields, models

class CancelWizard(models.TransientModel):
    _name = "hospital.cancel.appointment.wizard"
    _description = "hospital cancel appointment wizard"

