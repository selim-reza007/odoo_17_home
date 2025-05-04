

from dateutil.utils import today

from odoo import api, models, fields,_
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _order = "id desc"

    name = fields.Char("Name")
    age = fields.Integer(compute="_age_calculate", search="_search_age", inverse="inverse_age_calculate",string="Age")
    mobile = fields.Char("Contact no.")
    dob = fields.Date("Date of birth")
    image = fields.Image("Image")
    appointment_count = fields.Integer(compute="_compute_appointment",string="Appointment no.", store=True)
    appointments_ids = fields.One2many('hospital.appointment','patient_id',string="appointment line")
    is_birthday_today = fields.Boolean(string="Is Birthday Today?", compute="_compute_is_birthday_today")
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    website = fields.Char("Website")


    def execute_sql(self):
        query = """select name from hospital_patient where id = %s""" % self.id
        self.env.cr.execute(query)
        result = self.env.cr.dictfetchall()
        print(result)
        return

    @api.depends('dob')
    def _compute_is_birthday_today(self):
        today = fields.Date.context_today(self)  # Get today's date in the user's timezone
        for record in self:
            if record.dob:
                # Compare only the month and day of the DOB with today's date
                record.is_birthday_today = (record.dob.month == today.month) and (record.dob.day == today.day)
            else:
                record.is_birthday_today = False


    def _search_age(self, operator, value):
        dob = fields.Date.today() - relativedelta(years=value)
        start_of_year = dob.replace(day=1, month=1)
        end_of_year = dob.replace(day=31, month=12)
        return [('dob', '>=', start_of_year), ('dob', '<=', end_of_year)]

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

    # @api.depends('appointments_ids')
    # def _compute_appointment(self):
    #     for rec in self:
    #         rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.depends('appointments_ids')
    def _compute_appointment(self):
        appointment_group = self.env['hospital.appointment'].read_group(
            domain=[],groupby=['patient_id'],fields=['patient_id'])
        for appointment in appointment_group:
            patient_id = appointment.get('patient_id')[0]
            patient_rec = self.browse(patient_id)
            self -= patient_rec
        self.appointment_count = 0

    @api.constrains('dob')
    def _check_dob(self):
        for rec in self:
            if rec.dob and fields.Date.today() < rec.dob:
                raise ValidationError(_("Invalid Date of birth"))

    @api.onchange('dob')
    def _age_calculate(self):
        for rec in self:
            if rec.dob:
                rec.age = fields.Date.today().year - rec.dob.year
            else:
                rec.age = 1

    def btn_action(self):
        print("Clicked button")

    def action_view_appointments(self):
        return {
            'name': _('Appointments'),
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'context':{'default_patient_id':self.id},
            'domain':[('patient_id','=',self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }