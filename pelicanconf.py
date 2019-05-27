#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hammed Busirah Olaitan'
SITENAME = 'Datachick'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS = ['images', 'pdfs']
DISPLAY_PAGES_ON_MENU = True
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
 #        ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/hammedb197'),
          ('Twitter', 'https://twitter.com/h_bushroh'),
	  ('Linkedin', 'https://www.linkedin.com/in/hammedb/'),)

DEFAULT_PAGINATION = 10
#THEME = "/home/hammed/pelican-themes"
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FILES_TO_COPY = (('pelican-bgh/static/favicon.ico', 'favicon.ico'),) 
PLUGINS = ["pelican_resume",]

MENUITEMS = (
    ('CV', 'https://drive.google.com/file/d/1zRqcsQJrDvJIx38t-pWGWYKQ73Lf-14s/view?usp=sharing'),
)


#RESUME_PDF = "content/pdfs/HammedBusirahCV.pdf"
