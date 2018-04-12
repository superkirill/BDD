from behave import *
from app.generator import *

@given('Generator')
def step_impl(context):
    context.generator = Generator()

@when('the chord {chord} is requested')
def step_impl(context, chord):
    chord = chord.split(', ')
    if len(chord) == 2:
        context.chord = context.generator.get_chord(chord[0], chord[1])
    else:
        context.chord = context.generator.get_chord(chord[0])

@then('Generator returns {notes}')
def step_impl(context, notes):
    assert (context.chord == tuple(notes.split(', ')))

@when('the wrong chord {chord} is requested')
def step_impl(context, chord):
    chord = chord.split(', ')
    if len(chord) == 2:
        try:
            # do some loading here
            context.chord = context.generator.get_chord(chord[0], chord[1])
        except ValueError:
            context.chord = ValueError
    elif len(chord) == 2:
        try:
            # do some loading here
            context.chord = context.generator.get_chord(chord[0])
        except ValueError:
            context.chord = ValueError
    else:
        context.chord = ValueError



@then('Generator throws a ValueError')
def step_impl(context):
    assert (context.chord == ValueError)
