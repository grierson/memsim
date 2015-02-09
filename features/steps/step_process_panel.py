from behave import *

use_step_matcher("re")

@given("I what to create a new process")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    False


@when('I enter name: "(?P<process_name>.+)" with size: "(?P<process_size>.+)"')
def step_impl(context, process_name, process_size):
    """
    :type context behave.runner.Context
    :type process_name str
    :type process_size str
    """
    pass


@then('process "(?P<process_name>.+)" with "(?P<process_size>.+)" is created')
def step_impl(context, process_name, process_size):
    """
    :type context behave.runner.Context
    :type process_name str
    :type process_size str
    """
    pass