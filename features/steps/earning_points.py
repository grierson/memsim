""" Test flight points """
from behave import(
    given,
    when,
    then,
)

@given('the flying distance between {locA} and {locB} is {distance} km')
def given_distance_from_a_to_b(context):
    """step_impl

    :param context:
    """
    pass



@given('I am a standard Frequent Flyer member')
def given_i_am_member(context):
    """tep_impl

    :param context:
    """
    pass

@when('I fly from Sydney to Melbourne')
def when_fly_from_a_to_b(context):
    """step_impl

    :param context:
    """
    pass


@then('I should earn 439 points')
def then_should_earn_points(context):
    """step_impl

    :param context:
    """
    pass
