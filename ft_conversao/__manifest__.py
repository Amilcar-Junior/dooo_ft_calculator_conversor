# -*- coding: utf-8 -*-
{
    'name': "Calculadora",

    'summary': """
        Calculadora universal para fundamentos de telecomunicacao""",

    'description': """
        Calculadora universal para fundamentos de telecomunicacao
    """,

    'author': "Amilcar Junior",
    'website': "",

    'category': 'FT',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/ft_conversão_views.xml',
    ],

    'demo': [],
    'auto_install': True,
    'auto_update': True,
    'auto_upgrade': True,
    'installable': True,
    'application': True,
}
