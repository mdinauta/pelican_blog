AUTHOR = 'Matt DiNauta'
SITENAME = 'mdinauta.github.io'
SITEURL = 'http://mdinauta.github.io'
PATH = "content"
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ('LinkedIn', 'http://www.linkedin.com/pub/matt-dinauta/19/461/473'),
    ('Github', 'https://github.com/mdinauta'),
)

DEFAULT_PAGINATION = False
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-themes/tuxlite_tbs"