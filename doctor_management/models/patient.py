import datetime

from dateutil.utils import today

from odoo import api, models, fields,_
from odoo.odoo.tools.populate import compute
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char("Name")
    age = fields.Integer(compute="_age_calculate", inverse="inverse_age_calculate",string="Age")
    mobile = fields.Char("Contact no.")
    dob = fields.Date("Date of birth")
    appointment_count = fields.Integer(compute="_compute_appointment",string="Appointment no.", store=True)
    appointments_ids = fields.One2many('hospital.appointment','patient_id',string="appointment line")

    @api.depends('age')
    def inverse_age_calculate(self):
        today = fields.Date.today()
        for rec in self:
            rec.dob = today - relativedelta(years=rec.age)

    @api.ondelete(at_uninstall=True)
    def _check_appointment(self):
        for rec in self:
            if rec.appointments_ids:
                raise ValidationError(_("This patient record can't be deleted, this got an appointment."))

    @api.depends('appointments_ids')
    def _compute_appointment(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.constrains('dob')
    def _check_dob(self):
        for rec in self:
            if rec.dob and fields.Date.today() < rec.dob:
                raise ValidationError(_("Invalid Date of birth"))

    @api.onchange('dob')
    def _age_calculate(self):
        for rec in self:
            if rec.dob:
                rec.age = datetime.date.today().year - rec.dob.year
            else:
                rec.age = 1

    def btn_action(self):
        print("Clicked button")