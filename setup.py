from distutils.core import setup
import re

s = open('aherosms/version.py').read()
v = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", s, re.M).group(1)

setup(name='aherosms',
    version=v,
    description='Async API wrapper for hero-sms',
    install_requires=["aiohttp","certifi","aiohttp-socks"],
    author='optinsoft',
    author_email='optinsoft@gmail.com',
    keywords=['hero-sms','sms','async'],
    url='https://github.com/optinsoft/aherosms',
    packages=['aherosms']
)
