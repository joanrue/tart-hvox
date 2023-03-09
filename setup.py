#
# Author Tim Molteno 2017-2023 tim@elec.ac.nz
#
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='tart_hvox',
      version='0.0.1',
      description='TART-HVOX',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/joanrue/tart-hvox',
      author='Tim Molteno',
      test_suite='nose.collector',
      tests_require=['nose'],
      author_email='tim@elec.ac.nz',
      license='GPLv3',
      install_requires=['numpy', 'matplotlib',
                        'healpy', 'astropy', 'tart', 'disko', 'tart2ms'],
      packages=['tart_hvox'],
      scripts=['bin/hvox'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Scientific/Engineering",
          "Topic :: Communications :: Ham Radio",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3 :: Only',
          "Intended Audience :: Science/Research"])
