{
    'name': 'Custom sale',
    'application': False,
    'author': 'Selim Reza',
    'website': 'www.example.com',
    'data': [
        'reports/sale_order_template_inherit.xml',
        'views/inherited_sale_order_form.xml',
        'views/inherited_account_move_form.xml',
    ],
    'depends': ['sale','sale_management', 'account', 'mail'],
}