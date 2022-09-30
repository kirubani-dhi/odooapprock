# -*- coding: utf-8 -*-
# License: LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)
{
    'name': 'Read Only User Group Access Rights',
    'version': '12.0.1.0.1',
    'category': 'Access Rights',
    'author': 'KJ',
    'license': 'LGPL-3',
    'summary': """Group based access rights. This module is mainly used to provide the read only group access for specific user.
        Under the user setting, Made a new group as Read only Access.
        If we enabled such option, we restrict create, edit and delete for the all list view and form view.""",
    'description': """
        Group based access rights. This module is mainly used to provide the read only group access for specific user.
        Under the user setting, Made a new group as Read only Access.
        If we enabled such option, we restrict create, edit and delete for the all list view and form view.
    """,
    'depends': [
        'base',
    ],
    'data': [
        'security/security_groups.xml',
    ],
    'installable': True,
    'applicable': True,
    'auto_install': False,
    "images":['static/description/icon.png'],
    "live_test_url":'https://youtu.be/a5v9naRf7bY',
    'price': 5.00,
    'currency': 'EUR',
}
