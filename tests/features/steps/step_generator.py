from behave import *
from app.generator import *

@given('Generator')
def step_impl(context):
    context.generator = Generator()

@when('the chord is requested')
def step_impl(context):
    context.chord = context.generator.get_chord()

@then('Generator returns three notes')
def step_impl(context):
    assert (len(context.chord) == 3)