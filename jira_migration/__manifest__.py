# Copyright © 2021 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Jira Migration',
    'summary': 'Jira Migration',
    'category': 'Jira',
    "author": "Drake Bui",
    "website": "https://www.drakebui.ml/",
    'depends': [],
    "data": [
        'security/jira_security.xml',
        'security/ir.model.access.csv',

        'views/jira_project_views.xml',
        'views/jira_status_views.xml',
        'views/jira_time_logging_views.xml',

        'wizard/jira_logging_time_views',
    ],
    "application": True,
}
