try:
  from setuptools import setup
except ImportError:
  from disutils.core import setup

config = {
  'description': 'My project',
  'author': 'My name',
  'url': 'URL to get it',
  'download_url': 'where to download',
  'author_email': 'My email',
  'version': '0.1',
  'install_requires': ['gothonweb'],
  'packages': ['gothonweb'],
  'scripts': [],
  'name': 'gothonweb'
}

setup(**config)
