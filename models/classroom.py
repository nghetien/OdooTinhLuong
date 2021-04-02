# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Classroom(models.Model):
    _name = "classroom"
    _description = "Classroom"

    id_class = fields.Integer(string='Id Classroom', required=True,
         default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    number_class = fields.Char(string='Name Subject', required=True)
    id_subject = fields.Many2one('subject' ,string="Id Subject", required=True,
                              help="Subject",
                              states={'name_subject': [('readonly', False)]})
    id_teacher = fields.Many2one('teacher' , string="Id Teacher", required=True)
    quantity_student = fields.Integer(string="Quantity Student", required=True)