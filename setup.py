from distutils.core import setup

setup(
    name='wagtail-staging',
    version='0.1',
    packages=['staging', 'staging.management', 'staging.management.commands'],
    url='https://github.com/code-on/wagtail-staging',
    license='BSD licence, see LICENCE',
    description='Wagtail staging helpers',
    long_description=open('README.md').read()
)