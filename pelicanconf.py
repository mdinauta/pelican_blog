#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt DiNauta'
SITENAME = u'mdinauta.github.io'
SITEURL = 'http://mdinauta.github.io'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/pub/matt-dinauta/19/461/473'),
          ('Twitter', 'https://twitter.com/this_is_matt'),
          ('Github', 'https://github.com/mdinauta'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-themes/tuxlite_tbs"

MARKUP = ('md', 'ipynb')
PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

IGNORE_FILES = ['.ipynb_checkpoints']
