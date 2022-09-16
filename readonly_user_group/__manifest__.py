# -*- coding: utf-8 -*-
# License: LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)
{
    'name': 'Read only User Group',
    'version': '12.0.1.0.1',
    'category': 'Access Rights',
    'author': 'KJ',
    'license': 'LGPL-3',
    'summary': 'Add a special read only user group',
    'description': '''
        Made a new group as 'read only group'. If we enabled this option, we restrict create, edit and delete for the all list view. 
        This user only can able to see the records.
    ''',
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
    'price': 10.00,
    'currency': 'EUR',
    'website':'https://tintumon.co.in/'
}
