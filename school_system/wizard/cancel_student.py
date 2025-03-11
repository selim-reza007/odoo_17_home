from odoo import api, fields, models

class CancelStudentWizard(models.TransientModel):
    _name = 'school.student.cancel.wizard'
    _description = 'student cancel wizard'
    # _rec_name =

    student_id = fields.Many2one('school.student', "Select student")
    reason = fields.Char("Reason")