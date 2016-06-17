import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = []

tests_require = [
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='pymottainai',
      version='0.0',
      description='python implementation of the Mottainai rule set',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Wayne Witzel III',
      author_email='wayne@riotousliving.com',
      url='',
      keywords='games cards mottainai',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      )
