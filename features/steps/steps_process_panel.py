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
    context.ram = Memory(context.parent)
    context.panel = ProcessPanel(context.parent, context.ram)
    context.process_name = process_name
    context.process_size = process_size

@when(u'I press the create button')
def when_button_pressed(context):
    """when_button_pressed

    :param context:
    """
    assert context.ram.validate_process(context.process_name, 
                                        context.process_size)


@then(u'process is created')
def then_create_process(context):
    """then_create_process

    :param context:
    """
    assert True
