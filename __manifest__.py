{
    'name': 'HoReSo Attendances',
    'version': '1.0',
    'category': 'Human Resources/Attendances',
    'summary': 'HoReSo attendance',
    'description': 'Horeso Attendance',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employees_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}