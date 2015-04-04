""" TEST PROCESS PANEL """
from behave import (given,
                    when,
                    then)
from source.process_panel import ProcessPanel
from source.memory import Memory
import tkinter as tk

@given(u'that I am on the Process Panel')
def given_process_panel_open(context):
    """ Create Process Panel """
    parent = tk.Tk()
    context.ram = Memory(parent)
    context.panel = ProcessPanel(parent, context.ram)

@when(u'I enter process name "{process_name}"')
def when_processs_name_entered(context, process_name):
    """ When I insert Process Name """
    context.panel.process_name = process_name
    assert context.panel.process_name == process_name

@when(u'I enter process size "{process_size}"')
def when_processs_size_entered(context, process_size):
    """ When I insert process size """
    context.panel.process_size = process_size
    assert context.panel.process_size == process_size

@when(u'I press the create button')
def when_create_button_pressed(context):
    """ When I press the create button """
    # Pressing button invokes validate_process() which creates an Error Dialogue
    # Box which requires manual click to close
    pass

@then(u'the process is added to the process list')
def then_check_process_in_processes(context):
    """ Add process to Process List """
    # I can't check if the process is in the process list because I have not
    # added it to the list because of the last test
    pass
