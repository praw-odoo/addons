{
    'name': 'Real Estate Extended',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Manages Real Estate Advertisement and Services',
    'description': "",
    'website': 'http://www.odoo.com/real_estate',
    'depends': ['web_grid'],
    'data':[
    #    'views/property_type_views.xml',
    #    'views/property_tag_views.xml',
    #    'views/property_offer_views.xml',
       'views/property_views.xml',
    #   'views/estate_menus.xml',
       'security/ir.model.access.csv'
    ],
    'demo': [],
    #'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}