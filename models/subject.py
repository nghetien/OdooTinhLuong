# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Subject(models.Model):
    _name = "subject"
    _description = "Subject"

    id_subject = fields.Integer(string='Id Subject', required=True,
         default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    name_subject = fields.Char(string='Name Subject', required=True)
    coefficient_subject = fields.Float(string="Coefficient subject", required=True)