# -*- coding: utf-8 -*-
{
    'name': "website_demo_page",

    'summary': """
       Module for Odoo Course""",

    'description': """
        A demo page for Odoo Course
    """,

    'author': "Alexsandro Haag - HGSOFT",
    'website': "http://www.hgsoft.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'website',
    'version': '10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
