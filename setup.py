from setuptools import setup

setup(name                =  'pyoptical'                                   ,
      version             =  '0.1.0'                                       ,
      description         =  'Optics Library for Python'                   ,
      url                 =  'http://github.com/artemis-beta/pyoptical'    ,
      author              =  'Kristian Zarebski'                           ,
      author_email        =  'krizar312@yahoo.co.uk'                       ,
      license             =  'MIT'                                         ,
      packages            =  ['pyoptical']                                 ,
      zip_safe            =  False                                         ,
      tests_require       =  ['nose2']                                     ,
      install_requires    =  [ 'numpy>=1.11.3'      ,
                               'matplotlib>=2.0.0'  ,
                             ]
     )
