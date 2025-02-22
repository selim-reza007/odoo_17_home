# -*- coding: utf-8 -*-
from odoo import models, fields, api
from .constant import GENDER_SELECTION


class Parents(models.Model):
    _name = 'school.parents'
    _description = 'Parent module'

    name = fields.Char("Parent name")
    gender = fields.Selection(GENDER_SELECTION, string="Select gender")
    address = fields.Char("Address")
    occupation = fields.Char("Occupation")