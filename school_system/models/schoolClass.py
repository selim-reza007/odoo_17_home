from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = 'school.schoolclass'
    _description = 'school class module'

    name = fields.Char("Class name")
    capacity = fields.Integer("Max students")
    class_teacher = fields.Many2one('school.teacher', string="Class Teacher")
    subject_line_ids = fields.One2many('class.subject.line', 'classroom_id', string="Subjects")


class ClassSubjectLine(models.Model):
    _name = 'class.subject.line'
    _description = 'Class subject line'
    _rec_name = 'subject_id'

    subject_id = fields.Many2one('school.subjects', string="Select subject")
    teacher_id = fields.Many2one('school.teacher', string="Select teacher")
    schedule = fields.Char(string="Class time")
    classroom_id = fields.Many2one('school.schoolclass', string="Classroom")
