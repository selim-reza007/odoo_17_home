{
    'name' : 'Hospital sytem',
    'version' : '1.2',
    'sequence': -10,
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/doctor.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
