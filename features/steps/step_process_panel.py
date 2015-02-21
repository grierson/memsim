""" STEPS for Feature file """
from behave import (given,
                    then,
                    when)


@given("I what to create a new process")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    False


@when('I enter name: "{process_name}" with size: "{process_size}"')
def step_impl(context, process_name, process_size):
    """
    :type context behave.runner.Context
    :type process_name str
    :type process_size str
    """
    pass


@then('process "{process_name}" with "{process_size}" is created')
def step_impl(context, process_name, process_size):
    """
    :type context behave.runner.Context
    :type process_name str
    :type process_size str
    """
    pass
