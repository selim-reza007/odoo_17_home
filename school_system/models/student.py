# -*- coding: utf-8 -*-
from datetime import date
from email.policy import default
from odoo import models, fields, api
from .constant import GENDER_SELECTION


class Student(models.Model):
    _name = 'school.student'
    _description = 'school student module'

    name = fields.Char("Student name")
    dob = fields.Date("Date of birth")
    age = fields.Integer(compute="_compute_age", string="Age")
    gender = fields.Selection(GENDER_SELECTION, string="Select gender")
    parents_id = fields.Many2one('school.parents', string="Select parents")
    relation = fields.Char("Relation with parent")
    admission_date = fields.Date("Admission date", default=fields.Date.today())

    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                record.age = date.today().year - record.dob.year
            else:
                record.age = 1

    def cancel_studentship(self):
        return self.env.ref('school_system.action_cancel_student_wizard').read()[0]