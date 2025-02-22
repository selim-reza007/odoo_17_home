from odoo import models, fields, api

class SchoolClass(models.Model):
    _name = 'school.schoolclass'
    _description = 'school class module'

    name = fields.Char("Class name")
    capacity = fields.Integer("Max students")
    class_teacher = fields.Many2one('school.teacher', string="Class Teacher")
    subject_line_ids = fields.One2many('class.subject.line', 'classroom_id', string="Subjects")
    student_line_ids = fields.One2many('class.student.line','classroom_id','Students')

class ClassSubjectLine(models.Model):
    _name = 'class.subject.line'
    _description = 'Class subject line'
    _rec_name = 'subject_id'

    subject_id = fields.Many2one('school.subjects', string="Select subject")
    teacher_id = fields.Many2one('school.teacher', string="Select teacher")
    schedule = fields.Char(string="Class time")
    classroom_id = fields.Many2one('school.schoolclass', string="Classroom")

class classStudentLine(models.Model):
    _name = 'class.student.line'
    _description = 'Class student line'
    _rec_name = 'student_id'

    student_id = fields.Many2one('school.student', "Select student")
    class_roll = fields.Char("Class roll")
    classroom_id = fields.Many2one('school.schoolclass', string="Classroom")