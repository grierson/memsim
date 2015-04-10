""" STEPS process Panel """
from behave import (given,
                    when,
                    then)
from source.process_panel import ProcessPanel
from source.memory import Memory
import tkinter as tk

PARENT = tk.Tk()
RAM = Memory(PARENT)
PANEL = ProcessPanel(PARENT, RAM)

@given(u'"{process_name}" does not exist in memory')
def given_process_not_exist(context, process_name):
    assert RAM.check_process_exists(process_name) is False

@when(u'I enter process name "{process_name}"')
def when_enter_process_name(context, process_name):
    PANEL.process_name = process_name

@when(u'I enter process size "{process_size}"')
def when_enter_process_size(context, process_size):
    PANEL.process_size = process_size

@when(u'I press the create process button')
def when_press_button(context):
    RAM.validate_process(str(PANEL.process_name),
                         int(PANEL.process_size))

@then(u'"{process_name}" should be in memory')
def then_process_created(context, process_name):
    assert RAM.check_process_exists(process_name) is True
