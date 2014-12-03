""" Automate Commands """
from paver.tasks import task
from paver.easy import sh

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
