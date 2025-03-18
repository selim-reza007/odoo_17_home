import datetime
from odoo.exceptions import ValidationError
from odoo import api, fields, models,_

class CancelStudentWizard(models.TransientModel):
    _name = 'school.student.cancel.wizard'
    _description = 'student cancel wizard'
    # _rec_name =

    student_id = fields.Many2one('school.student', "Select student")
    reason = fields.Char("Reason")
    cancel_date = fields.Date("Cancel Date")

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['student_id'] = self.env.context.get('active_id')
        res['cancel_date'] = datetime.date.today()
        return res

    def action_cancel(self):
        if self.student_id.admission_date == fields.Date.today():
            raise ValidationError(_("Admission and cancel can't be same!"))
        return

    def discard_process(self):
        return
