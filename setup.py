from distutils.core import setup

setup(
    name='gosttpy',
    version='0.1.0',
    author='fito_segrera',
    author_email='fitosegrera@gmail.com',
    packages=['gosttpy'],
    scripts=['bin/example.py'],
    url='http://pypi.python.org/pypi/gosttpy/',
    license='LICENSE.txt',
    description='Python module for speech recognition using Google speech recognition API',
    long_description=open('README.txt').read(),
    install_requires=[
        "simplejson==3.4.0",
    ],
)