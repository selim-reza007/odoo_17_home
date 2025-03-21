import datetime
from odoo import api, models, fields
from odoo.odoo.tools.populate import compute


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'

    name = fields.Char("Name")
    age = fields.Integer(compute="_age_calculate",string="Age")
    mobile = fields.Char("Contact no.")
    dob = fields.Date("Date of birth")

    @api.onchange('dob')
    def _age_calculate(self):
        for rec in self:
            if rec.dob:
                rec.age = datetime.date.today().year - rec.dob.year
            else:
                rec.age = 1