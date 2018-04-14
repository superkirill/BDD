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
    context.play = context.generator.play(note=note, octave=float(octave))

@when ('it tries to play an incorrect chord {chord}')
def step_impl(context, chord):
    context.play = context.generator.play(chord=tuple(chord.split(', ')))

@when ('it tries to play a note in an incorrect octave {octave}')
def step_impl(context, octave):
    context.play = context.generator.play(note='C', octave=octave)

@when('it tries to play on an incorrect instrument {instrument}')
def step_impl(context, instrument):
    context.play = context.generator.play(note='C', instrument=instrument)

@when('it tries to play with incorrect duration {duration}')
def step_impl(context, duration):
    context.play = context.generator.play(note='C', duration=duration)

@when('it is asked to generate a melody based on progression E minor, D, G, C, E minor')
def step_impl(context):
    chord_dur = [1, 0.2]
    pause = [0.15, 1]
    progression = [(context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('D', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('D', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('G', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('G', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('C', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('C', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   ]
    context.melody = context.generator.get_melody(progression)


@then('it returns a non-empty list of notes at least once over 100 attempts')
def step_impl(context):
    context.melody = [context.melody] if len(context.melody) !=0 else []
    chord_dur = [1, 0.2]
    pause = [0.15, 1]
    progression = [(context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('D', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('D', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('G', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('G', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('C', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('C', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   ]
    for i in range(100):
        melody = context.generator.get_melody(progression)
        if len(melody) != 0:
            context.melody.append(context.generator.get_melody(progression))
    assert (len(context.melody) != 0)



@when('it is asked to generate a melody based on an incorrect progression {progression}')
def step_impl(context, progression):
    context.melody = context.generator.get_melody(progression)
    print(context.melody)

@then('it shows that something went wrong!')
def step_impl(context):
    assert (context.melody == False)

@when('it is asked to generate a melody with incorrect amount of max allowed notes {max}')
def step_impl(context, max):
    chord_dur = [1, 0.2]
    pause = [0.15, 1]
    progression = [(context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('D', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('D', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('G', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('G', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('C', 'major'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('C', 'major'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (context.generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (context.generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   ]
    context.melody = context.generator.get_melody(progression, max_notes=max)

@when('it is asked to perform a track {track}')
def step_impl(context, track):
    context.perform = context.generator.perform(track)

@then('it performs it and signals that everything is fine')
def step_impl(context):
    assert (context.perform == True)

