from behave import *
from app.generator import *

@given('Generator')
def step_impl(context):
    context.generator = Generator()

@when('the chord {chord} is requested')
def step_impl(context, chord):
    context.chord = context.generator.get_chord(str(chord))

@then('Generator returns {notes}')
def step_impl(context, notes):
    assert (context.chord == tuple(notes.split(', ')))