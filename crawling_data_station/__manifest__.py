# Copyright © 2021 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Drake Bui: Crawling Product Station',
    'summary': 'Drake Bui: Crawling Product Station',
    'category': 'Drake Bui',
    "author": "Drake Bui",
    "website": "https://www.drakebui.ml/",
    'depends': [
        'lunch'
    ],
    "data": [
        'security/ir.model.access.csv',
        
        'views/crawling_station_views.xml',
        'views/crawling_tag_views.xml',

        'views/menus.xml',
    ],
    "application": False,
    "installable": True,
    'assets': {},
}
