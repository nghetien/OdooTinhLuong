# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date, datetime, time
from datetime import timedelta
from openerp.tools.translate import _


class Course(models.Model):
    _name = "course"
    _description = "Course"
    _rec_name = "name_course"

    id_course = fields.Char(string='Mã lớp học', readonly=True)
    name_course = fields.Char(string='Tên lớp học', required=True)
    semester = fields.Many2one('semester', string="Kỳ học")

    id_teacher = fields.Many2one('teacher', string="Mã giáo viên giảng dạy", required=True)
    name_teacher = fields.Char(string='Tên giáo viên giảng dạy', related='id_teacher.name_teacher', readonly=True)
    department_of_teacher = fields.Many2one('department', string='Khoa chủ quản giáo viên', related='id_teacher.name_department', readonly=True)
    rank_teacher = fields.Many2one('coefficient.teacher', string='Học hàm của giáo viên', related='id_teacher.rank', readonly=True)
    coefficient_teacher = fields.Float(string='Hệ số học hàm', related='id_teacher.coefficient_teacher', readonly=True)

    id_subject = fields.Many2one('subject', string="Mã môn học", required=True)
    name_subject = fields.Char(string='Tên môn học', related='id_subject.name_subject', readonly=True)
    rank_subject = fields.Many2one('coefficient.subject', string='Độ khó', related='id_subject.rank', readonly=True)
    coefficient_subject = fields.Float(string='Hệ số môn học', related='id_subject.coefficient_subject', readonly=True)
    course_sequence = fields.Char(string='Mã lớp học tăng', required=True, copy=False,
                                        readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        vals['course_sequence'] = self.env['ir.sequence'].next_by_code('course.sequence')
        vals['id_course'] = str(vals['name_course']) + vals['course_sequence']
        result = super(Course, self).create(vals)
        return result