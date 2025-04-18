from odoo import api, fields, models

class Operation(models.Model):
    _name = 'hospital.operation'
    _description = 'hospital operation'
    _log_access = False

    doctor_id = fields.Many2one("doctor.doctor", string="Doctor")