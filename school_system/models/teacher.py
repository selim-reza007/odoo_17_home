# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
from .constant import GENDER_SELECTION


class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'school teacher module'

    name = fields.Char("Teacher name")
    gender = fields.Selection(GENDER_SELECTION, "Select gender")
    dob = fields.Date("Date of Birth")
    education = fields.Selection([
        ("masters","Masters"),
        ("honors","Honors"),
        ("degree","Degree")
    ], string="Educational Qualification")
    address = fields.Char("Address")
    marital_status = fields.Selection([
        ('single','Single'),
        ('Married','Married'),
        ('unknown','Unknown'),
    ])