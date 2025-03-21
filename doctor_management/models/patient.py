import datetime
from odoo import api, models, fields,_
from odoo.odoo.tools.populate import compute
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char("Name")
    age = fields.Integer(compute="_age_calculate",string="Age")
    mobile = fields.Char("Contact no.")
    dob = fields.Date("Date of birth")

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