""" Automate Commands """
from paver.easy import *
import paver.doctools
from paver.tasks import task
from pip.req import parse_requirements
from paver.setuputils import (
    setup,
    install_distutils_tasks
)
from distutils.core import setup

# -- REQUIRED-FOR: setup, sdist, ...
# NOTE: Adds a lot more python-project related tasks.
install_distutils_tasks()


# ----------------------------------------------------------------------------
# PROJECT CONFIGURATION (for sdist/setup mostly):
# ----------------------------------------------------------------------------
NAME    = "MemSim"
VERSION = open("VERSION.txt").read().strip()
DESCRIPTION = "Memory Mangement Simulator"
REQUIRES = parse_requirements("requirements.txt")
INSTALL_REQUIRES = [str(r.req) for r in REQUIRES]

CLASSIFIERS = """\
Development Status :: 4 - Beta
Environment :: Console
Framework :: behave
Intended Audience :: Developers
License :: OSI Approved :: New BSD License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Topic :: Software Development
Topic :: Documentation
Topic :: Education
"""

# ----------------------------------------------------------------------------
# TASK CONFIGURATION:
# ----------------------------------------------------------------------------
options(
    setup= dict(
        name = NAME,
        version = VERSION,
        url="http://pypi.python.org/pypi/%s/" % NAME,
        author="Kyle Grierson",
        author_email="grierson@openmailbox.net",
        license="BSD",
        description= DESCRIPTION,
        keywords   = "utility",
        platforms  = [ 'any' ],
        classifiers= CLASSIFIERS.splitlines(),
        install_requires= INSTALL_REQUIRES,
        include_package_data= True,
    ),
    minilib=Bunch(
        extra_files=[ 'doctools', 'virtual' ]
    ),
    pip = Bunch(
        requirements_files=[
            "requirements.txt",
        ],
    ),
    test=Bunch(
        default_args=[
            "features/",
        ],
        behave_formatter = "progress",
    ),
    pylint    = Bunch(default_args=NAME),
)


@task
def unit():
    """unit_test"""
    sh('py.test test/')

@task
def bdd():
    """bdd"""
    sh('behave')

@task
def report_pylint():
    """lint"""
    sh('pylint --msg-template="{path}:{line}:[{msg_id}({symbol}), {obj}] {msg}" memsim/ > reports/pylint.txt')

@task
def report_cov():
    """cov"""
    sh('py.test --cov-report xml --cov=memsim/')
    sh('mv coverage.xml reports/.')

@needs('report_cov','report_pylint')
def report():
    pass
