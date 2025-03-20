{
    'name' : 'Hospital sytem',
    'version' : '1.2',
    'sequence': -10,
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/appointment_sequence_data.xml',
        'views/menu.xml',
        'views/doctor.xml',
        'views/days.xml',
        'views/patient.xml',
        'views/appointment.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
