""" Steps for Process Feature """
from behave import (
    given,
    when,
    then
)

@given('I enter Firefox')
def givent_firefox(context):
    """givent_firefox

    :param context:
    """
    assert True

@given('I enter 100')
def given_enter_100(context):
    """given_enter_100

    :param context:
    """
    assert True

@when('I press create process')
def when_create_process(context):
    """when_create_process

    :param context:
    """
    assert True

@then('a process with Firefox and 100 should be created')
def then_firefox_created(context):
    """then_firefox_created

    :param context:
    """
    assert True
