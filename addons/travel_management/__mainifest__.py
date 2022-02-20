{
    'name': 'Travel Management',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Manages Travel Management Services',
    'description': "",
    'website': 'http://www.odoo.com/real_estate',
    'depends': ['web_grid'],
    'data':[
        'security/ir.model.access.csv',
        'views/travel_views.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}