""" Process Panel Step File """
from memsim.process_panel import ProcessPanel
import tkinter

@given(u'I what to create a new process')
def given_i_want_to_create_process(context):
    """given_i_want_to_create_process

    :param context:
    """
    pass

@when(u'I enter name: "{process_name}" with size: "{process_size}"')
def when_i_enter_process_details(context, process_name, process_size):
    """when_i_enter_process_details

    :param context:
    """
    new_panel = ProcessPanel(tkinter.Tk())
    new_panel.process_name = process_name
    new_panel.process_size = process_size
    new_panel.check_process_details()


@then(u'process "{process_name}" with "{process_size}" is created')
def then_process_is_created(context, process_name, process_size):
    """then_a_new_process_is_created

    :param context:
    """
    pass
