""" TEST PROCESS PANEL """
from behave import (given,
                    when,
                    then)
from memsim.process_panel import ProcessPanel
from memsim.memory import Memory
import tkinter as tk

@given(u'I enter process details "{process_name}", "{process_size}"')
def given_process_details(context, process_name, process_size):
    """given_process_details

    :param context:
    :param process_name:
    :param process_size:
    """
    context.parent = tk.Tk()
    ram = Memory(context.parent)
    context.panel = ProcessPanel(context.parent, ram)
    context.panel.process_name = process_name
    context.panel.process_size = process_size

@when(u'I press the create button')
def when_button_pressed(context):
    """when_button_pressed

    :param context:
    """
    raise NotImplementedError(u'STEP: When I press the create button')

@then(u'process "{process_name}", "{process_size}" is created')
def then_create_process(context, process_name, process_size):
    """then_create_process

    :param context:
    :param process_name:
    :param process_size:
    """
    raise NotImplementedError(u'STEP: Then process "Calculator", "100" is created')

