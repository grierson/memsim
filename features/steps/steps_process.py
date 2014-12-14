""" Step file for Process """
from behave import (
    given,
    when,
    then,
)

@given(u'I enter "<process_name>" with "<process_size>"')
def given_process_data(context, process_name, process_size):
    """given_process_data

    :param context:
    :param process_name:
    :param process_size:
    """
    assert True

@when(u'I press create process')
def when_button_pressed(context):
    """when_button_pressed

    :param context:
    """
    assert True

@then(u'a process with "<process_name>" with "<process_size>" is created')
def then_process_created(context, process_name, process_size):
    """then_process_created

    :param context:
    :param process_name:
    :param process_size:
    """
    assert True
