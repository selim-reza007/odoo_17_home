from odoo import api, fields, models

class Operation(models.Model):
    _name = 'hospital.operation'
    _description = 'hospital operation'
    _log_access = False
    _order = 'sequence, id'

    doctor_id = fields.Many2one("doctor.doctor", string="Doctor")
    operation_name = fields.Char("Name")
    reference_record = fields.Reference(selection=[('hospital.patient','Patient'), ('hospital.appointment','Appointment')], string='Record')
    sequence = fields.Integer(string="Sequence", default=10)

    @api.model
    def name_create(self, name):
        record = self.create({'operation_name': name})
        return record.id, record.display_name