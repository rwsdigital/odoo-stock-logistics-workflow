# -*- coding: utf-8 -*-
# © 2018 RWSdigital (https://www.rwsdigital.com)
#   @author Antonio Russo <antonio.r@rwsdigital.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Fast Products Quantity Search',
    'summary': """Currently search product by quantity is very slow.
    With this module search time is incredibly faster!
        """,
    'version': '10.0.0.1.0',
    'author': "RWSdigital",
    'website': 'https://www.rwsdigital.com',
    'category': 'Warehouse',
    'depends': [
        'stock',
        'product',
    ],
    "data"                 :  [
                             'views/product_views.xml',
                            ],
    'application': False,
    'installable': True,
}
