# -*- coding: utf-8 -*-
{
    'name': "itzain_payment_action",
    'summary': "Adding Server Action In Point_Of_Sale ",
    'description': """
Add payment server action in point_of_sale
    """,
    'author': "Ahmed Zaki",
    'website': "http://www.itzain.com",
    'category': 'point_of_sale',
    'version': '17.0.0.0',
    'depends': ['base','point_of_sale'],
    'data': [
        'views/pos_order_server_action_views.xml',
    ],
}

