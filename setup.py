#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="pre-commit-django-uncommitted-migrations",
    version="0.0.1",

    author="Sam Nicholls",
    author_email="sam@samnicholls.net",

    packages=setuptools.find_packages(),
    install_requires=[],

    entry_points = {
        'console_scripts': [
            'check_migrations = check_migrations.main:main',
        ]
    },

)
