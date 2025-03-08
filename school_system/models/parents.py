# -*- coding: utf-8 -*-
from odoo import models, fields, api
from .constant import GENDER_SELECTION


class Parents(models.Model):
    _name = 'school.parents'
    _description = 'Parent module'
    # _rec_name = 'name'

    name = fields.Char("Parent name")
    gender = fields.Selection(GENDER_SELECTION, string="Select gender")
    address = fields.Char("Address")
    occupation = fields.Char("Occupation")

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.occupation} {record.name}"


   # depreciated after Odoo 17 but was worked fine before Odoo 17
    # def name_get(self):
    #     parents_list = []
    #     for record in self:
    #         name = record.occupation + ' ' + record.name
    #         parents_list.append((record.id, name))
    #     return parents_list
