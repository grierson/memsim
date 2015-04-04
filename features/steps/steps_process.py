""" TEST PROCESS """
from behave import (given,
                    when,
                    then,)
from source.memory import Memory
import tkinter as tk

@given(u'process name "{name}"')
def given_process_name(context, name):
    """ Given Process Name """
    context.name = name

@given(u'process size "{size}"')
def given_process_size(context, size):
    """ Given Process Size """
    context.size = size

@given(u'process address "{address}"')
def given_process_address(context, address):
    """ Given Process Address """
    context.address = address

@when(u'I create the process')
def when_i_create_process(context):
    """ When I create the process """
    context.ram = Memory(tk.Tk())
    context.ram.create_process(context.name,
                               context.size,
                               context.address)

@then(u'a process with the name "{name}"')
def then_process_has_name(context, name):
    """ Then the process has the name """
    assert context.ram.check_process_exists(name) is True

@then(u'process size "{size}"')
def then_process_has_size(context, size):
    """ Then the process has the size """
    assert context.ram.get_process_size(context.name) == size

@then(u'should be at "{address}"')
def then_process_has_address(context, address):
    """ Then the process has the address """
    assert context.ram.get_process_address(context.name) == address
