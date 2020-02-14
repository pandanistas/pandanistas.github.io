#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Author'
SITENAME = 'Pandanistas'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme Settings
THEME = 'themes/brutalist_2'
## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'site-cover.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'pandanistas website.'
## path to favicon
# FAVICON = 'pelly.png'
## path to logo for nav menu (optional)
# LOGO = 'pelly.png'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'pandanistas'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
# TWITTER_USERNAME = '@mcman_s'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
# ATTRIBUTION = True
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [('tags', '/tags')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example
TWITTER = 'https://twitter.com/'
