import os
from setuptools import setup, find_packages

from tiamat import __doc__, __version__, __author__, __email__


desc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name='django-tiamat',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/rvause/django-tiamat',
    description=__doc__,
    long_description=desc,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django >= 1.4'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'
    ],
    test_suite='tiamat.tests.run_tests.run_tests',
    tests_require=['Django']
)
