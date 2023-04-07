# -*- coding: utf-8 -*-
{
    'name': "Carburant",

    'summary': """
       Module de gestion de carburant""",

    'description': """
        Module de Gestion carburant
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'fleet'],

    # always loaded
    'data': [
        'security/carburant_groupes.xml',
        'security/ir.model.access.csv',
        'views/chargement_views.xml',
        'views/consommation_views.xml',
        'views/cartecarburant_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
