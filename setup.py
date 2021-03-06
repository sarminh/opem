# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
  name = 'opem',
  packages = ['opem'],
  version = '0.1',
  description = 'Open Source PEM Cell Simulation Tool',
  long_description='''Open Source PEM Cell Simulation Tool''',
  author = 'Sepand Haghighi,Kasra Askari,Sarmin Hamidi,Mohammad Mahdi Rahimi',
  author_email = 'opem@ecsim.ir',
  url = 'https://github.com/ecsim/opem',
  download_url = 'https://github.com/ecsim/opem/tarball/v0.1',
  keywords = ["OPEM","PEM","FC","CELL","Fuel Cell"],
  install_requires=[
      'art',
	  'codecov',
      'requests',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
    ],
  license='MIT',
)
