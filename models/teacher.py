# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Teacher(models.Model):
    _name = "teacher"
    _description = "Professor Teacher"

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, 
                                readonly=True, help="Employee",
                                states={'draft': [('readonly', False)]})
    id_teacher = fields.Char(string='Id Teacher', required=True, )
    name_teacher = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('orther', 'Orther'),
    ], required=True, default='male',)
    coefficient_teacher = fields.Float(string='Coefficient Teacher', required=True)

