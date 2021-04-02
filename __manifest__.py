# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Tính Lương giáo viên',
    'version' : '1.1',
    'summary': 'Tính lương',
    'sequence': 10,
    'description': """Tính lương cho giảng viên theo giờ dạy""",
    'category': 'Generic Modules/Human Resources',
    'website': 'https://www.odoo.com/page/tinh-luong',
    'depends' : [],
    'data': [
        'views/department.xml',
        'views/major.xml',
        'views/professor.xml',
        'views/coefficient_teacher.xml',
        'views/coefficient_subject.xml',
        'views/subject.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
