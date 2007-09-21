__version__ = '0.1'

import os
from setuptools import setup, find_packages

setup(name='repoze.vhm',
      version=__version__,
      description='repoze virtual hosting middleware.',
      long_description='',
      classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Framework :: Zope3",
        ],
      keywords='web application server wsgi zope repoze',
      author="Agendaless Consulting",
      author_email="repoze-dev@lists.repoze.org",
      dependency_links=['http://dist.repoze.org'],
      url="http://www.repoze.org",
      license="BSD-derived (http://www.dist.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['repoze'],
      zip_safe=False,
      install_requires=['zopelib >= 2.10.4.2',
                       ],
      test_suite = "repoze.vhm.tests",
      entry_points="""
      [paste.filter_app_factory]
      vhm_zope2 = repoze.vhm.zope2:make_filter
      vhm_xheaders = repoze.vhm.xheaders:make_filter
      """,
      )