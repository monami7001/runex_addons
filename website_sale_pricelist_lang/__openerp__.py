# -*- coding: utf-8 -*-

{
    'name': 'eCommerce lang Price-list',
    'version': '1.0',
    'author': 'Linserv AB',
    'sequence': 1,
    'website': 'www.linserv.se',
    'summary': 'change pricelist and currency when lang is changed',
    'contributors': [
        'Azer GHADHOUN <ghadhoun.azer@gmail.com>'
    ],
    'description': """
    """,
    'depends': ['website_sale'],
    'data': [
        'views/views.xml',
        'views/website_sale_template.xml',
    ],
    'installable': True,
    'auto_install': False,
}

