{
    'name' : 'Hospital sytem',
    'version' : '1.2',
    'sequence': -10,
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/appointment_sequence_data.xml',
        'wizard/cancel_appointment_wizard.xml',
        'views/menu.xml',
        'views/doctor.xml',
        'views/days.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/tags.xml',
        'views/configuration.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
