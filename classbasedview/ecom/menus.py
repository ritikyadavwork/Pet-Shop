MENUS = {
    'NAV_MENU_LEFT': [
        {
            "name": "Home",
            "icon_class": '',
            "url": "#",
            "validators": ['menu_generator.validators.is_superuser'],
            'submenu': [
                {
                    "name": "Company",
                    "url": "#",
                }
            ]
        },
        {
            "name": "About",
            "icon_class": '',
            "url": "#",
            "validators": ['menu_generator.validators.is_superuser'],
        },
        {
            "name": "Contact Us",
            "icon_class": '',
            "url": "#",
            "validators": ['menu_generator.validators.is_superuser'],
        }
    ],
    'NAV_MENU_RIGHT': [
        {
            "name": "Home",
            "icon_class": '',
            "url": "#",
            "validators": ['menu_generator.validators.is_superuser'],
            'submenu': [
                {
                    'name': 'Change Password',
                    'icon_class': '',
                    "url": "account_change_password",
                    "validators": ['menu_generator.validators.is_authenticated'],
                },
                {
                    "name": "Two Factor Authentication",
                    "url": "mfa_index",
                    "validators": ['menu_generator.validators.is_authenticated']
                },
                {
                    'name': 'Logout',
                    'icon_class': '',
                    'url': 'account_logout',
                    'validators': ['menu_generator.validators.is_authenticated'],
                }
            ]
        },
    ]
}
