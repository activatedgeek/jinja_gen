import sys
from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
MIN_PYTHON = (3, 6)

if CURRENT_PYTHON < MIN_PYTHON:
    sys.stderr.write("""
        ============================
        Unsupported Python Version
        ============================

        Python {}.{} is unsupported. Please use a version newer than Python {}.{}.
    """.format(*CURRENT_PYTHON, *MIN_PYTHON))
    sys.exit(1)

with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

with open('VERSION') as f:
    VERSION = f.read().strip()

with open('README.md') as f:
    README = f.read()

setup(name='jinja-gen',
      version=VERSION,
      description='Generate script files from easy configs',
      long_description=README,
      long_description_content_type='text/markdown',
      url='https://github.com/activatedgeek/jinja_gen',
      author='Sanyam Kapoor',
      license='MIT',
      classifiers=[
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
      ],
      packages=find_packages(),
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'jinja-gen=jinja_gen.cli:main',
          ],
      },
      zip_safe=False)
