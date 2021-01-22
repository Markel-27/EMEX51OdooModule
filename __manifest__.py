# -*- coding: utf-8 -*-
{
    'name': "Area 51",

    'summary': """
        Gestion de los empleados del area 51""",

    'description': """
        La gestion del area 51
    """,

    'author': "EMEX51",
    'website': "http://www.EMEX51.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/Markel-27/EMEX51OdooModule.git
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/emex51.xml',
        'views/armyviews.xml',
        'views/bossviews.xml',
        'views/employeeviews.xml',
        'views/sectoremployeesviews.xml',
        'views/creatureviews.xml',
        'views/visitorviews.xml',
        'views/sectorviews.xml',
        'views/menu.xml',
        'report/reportModule.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}