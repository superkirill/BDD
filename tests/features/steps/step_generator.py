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

@when ('it is asked to play a note {note}')
def step_impl(context, note):
    context.play = context.generator.play(note=note)

@then('it plays it and signals that everything is okay')
def step_impl(context):
    assert (context.play == True)

@when ('it is asked to play a horrible incorrect note {bad_note}')
def step_impl(context, bad_note):
    context.play = context.generator.play(note=bad_note)

@then('it shows that something went wrong')
def step_impl(context):
    assert (context.play == False)

@when ('it is asked to play a chord {chord}')
def step_impl(context, chord):
    context.play = context.generator.play(chord=tuple(chord.split(', ')))

@when ('it is required to play a note {note} with a specific {instrument}')
def step_impl(context, note, instrument):
    context.play = context.generator.play(note=note, instrument=int(instrument))

@when ('it is needed to play a note {note} with specific {duration}')
def step_impl(context, note, duration):
    context.play = context.generator.play(note=note, duration=float(duration))

@when ('it should play a note {note} in a specific {octave}')
def step_impl(context, note, octave):
    context.play = context.generator.play(note=note, octave=octave)
