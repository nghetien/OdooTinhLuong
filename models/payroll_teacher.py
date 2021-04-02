# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PayrollTeacher(models.Model):
    _name = "payroll.teacher"
    _description = "Payroll Teacher"

    name = fields.Char(string='Name', required=True)
    id_teacher = fields.Char(string='Id Teacher', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('orther', 'Orther'),
    ], required=True, default='male',)
    note = fields.Text(string='Description')

