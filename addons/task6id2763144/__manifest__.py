{
    'name': 'task 6',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'modify task 6',
    'description': "modify task 6",
    'website': 'http://www.odoo.com/task6',
    'depends': ['contacts','product','sale','sale_management','stock'],
    'data':[
        'views/InternTask_views.xml',
        #'security/InternTask_security_views.xml'
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}