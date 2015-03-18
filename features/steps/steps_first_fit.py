""" Test First Fit Allocation """
from behave import (given,
                      when,
                      then)
import source.first_fit


@given(u'process size {process_size}')
def step_impl(context, process_size):
    context.process_size = process_size

@when(u'hole equals {process_size}')
def step_impl(context, process_size):
    context.alloc = first_fit(context.process_size)

@then(u'allocate process to that address')
def step_impl(context):
    assert context.alloc is True

