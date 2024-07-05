{
    'name': 'Todo List',
    'version': '17.0.1.0.1',
    'category': 'Todo Lit',
    'summary': """Todo List""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/owl_temp.xml',
        # 'views/todo_list.xml',
        # 'views/todo_view.xml',
    ],
    'assets': {
        'web.assets_backend':[
            #JS
            # 'owl/static/src/components/todo_list/todo_list.js'
        ]
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
