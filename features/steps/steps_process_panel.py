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

@when(u'I enter process details "{process_name}"')
def when_processs_name_entered(context, process_name):
    """ When I insert Process Name """
    context.panel.process_name = process_name
    assert context.panel.process_name == process_name

@when(u'i enter process size "{process_size}"')
def when_processs_size_entered(context, process_size):
    """ When I insert process size """
    context.panel.process_size = process_size
    assert context.panel.process_size == process_size

@when(u'I press the create button')
def when_create_button_pressed(context):
    """ When I press the create button """
    context.panel.create_button.invoke()

@then(u'process is added to the process list')
def then_check_process_in_processes(context):
    """ Add process to Process List """
    assert context.ram.check_process_exists(context.panel.process_name)
