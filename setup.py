from setuptools import setup, find_packages, Extension
import sys
import os


__version__ = '1.0.8'


include_dirs = ['/usr/local/opt/openssl/include'] if sys.platform == "darwin" else []

upc_keys = Extension('upc_keys',
                     sources=['upc_keys.c'],
                     libraries=['crypto'],
                     include_dirs=include_dirs,)


def read_file(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), filename)) as f:
            return f.read()
    except IOError:
        return ''


setup(
    name='crackupc',
    packages=find_packages(),
    version=__version__,
    description='upc_keys.py -- WPA2 passphrase recovery tool for UPC%07d devices',
    long_description=read_file('README.md'),
    author='dsc',
    author_email='sander@cedsys.nl',
    url='https://github.com/skftn/upc_keys.py/',
    download_url='https://github.com/skftn/upc_keys.py/tarball/v%s' % __version__,
    include_package_data=True,
    zip_safe=False,
    ext_modules=[upc_keys],
    entry_points={
        'console_scripts': [
            'crack-upc=crack_upc.__main__:Main',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],
)
