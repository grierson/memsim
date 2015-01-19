""" Process Step File """
from behave import (
    given,
    when,
    then,
)
from memsim.process import Process

@given(u'I enter "{process_name}" with "{process_size}"')
def given_i_enter_process_details(context, process_name, process_size):
    """step_impl

    :param context:
    :param process_name:
    :param process_size:
    """
    if process_name.isalpha() and process_size.isdigit():
        pass
    else:
        raise "Process unacceptable"

@when(u'I press create process')
def when_i_create_a_process(context):
    """step_impl

    :param context:
    """
    new_process = Process(new_process_name, new_process_size)

@then(u'a process with "{process_name}" with "{process_size}" is created')
def then_a_process_is_created(context, process_name, process_size):
    """step_impl

    :param context:
    :param process_name:
    :param process_size:
    """
    new_process.get_process_name()
    new_process.get_process_size()
