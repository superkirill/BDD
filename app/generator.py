import pygame.midi
import time
from numpy import random as rd
import random
import os, sys
import ast
import subprocess

class Generator():
    """
        Generates chords and melodies
    """
    def __init__(self):
        self.intervals = {
            'C': 0,
            'C#': 1,
            'C##': 2,
            'D': 2,
            'Db': 1,
            'Dbb': 0,
            'D#': 3,
            'D##': 4,
            'E': 4,
            'Eb': 3,
            'Ebb': 2,
            'E#': 5,
            'E##': 6,
            'F': 5,
            'Fb': 4,
            'Fbb': 5,
            'F#': 6,
            'F##': 7,
            'G': 7,
            'Gb': 6,
            'Gbb': 5,
            'G#': 8,
            'G##': 9,
            'A': 9,
            'Ab': 8,
            'Abb': 7,
            'A#': 10,
            'A##': 11,
            'B': 11,
            'Bb': 10,
            'Bbb': 9,
            'B#': 12,
            'B##': 13
        }
        self.notes = {
            0: 'C',
            1: 'C#',
            2: 'D',
            3: 'D#',
            4: 'E',
            5: 'F',
            6: 'F#',
            7: 'G',
            8: 'G#',
            9: 'A',
            10: 'A#',
            11: 'B',
        }
        pygame.midi.init()
        self.player = pygame.midi.Output(0, 0)
        self.player.set_instrument(0)

    def get_chord(self, root='C', type='major'):
        """
            Generate a chord

            Keyword arguments:
                root -- capital letter from A to G, (default 'C')
                type -- string representing the type of chord:
                    major, minor, diminished or augmented (default 'major')
            Return:
                tuple of three notes the chord consists of, e.g. ('C', 'E', 'G')
        """
        if root not in self.intervals.keys() or type not in ['major','minor']:
            raise ValueError
        if type == 'major':
            third = self.intervals[root] + 4
            if third >= 12:
                third -= 12
            third = self.notes[third]
            fifth = self.intervals[root] + 7
            if fifth >= 12:
                fifth -= 12
            fifth = self.notes[fifth]
            return (root, third, fifth)
        elif type == 'minor':
            third = self.intervals[root] + 3
            if third >= 12:
                third -= 12
            third = self.notes[third]
            fifth = self.intervals[root] + 7
            if fifth >= 12:
                fifth -= 12
            fifth = self.notes[fifth]
            return (root, third, fifth)

    def play(self, note=None, chord=None, octave=3, duration=0.5, instrument=0):
        """
            Play a note

            Keyword arguments:
                note -- capital letter from A to G, (default None)
                chord -- tuple representing a chord to be played (default None)
                instrument -- integer representing a pygame.midi instrument (default 0)
                duration -- double representing amount of time during which the note
                    or the chord should sound
            Return:
                True -- if the note was played successfully
                False -- if some arg did not match the specification
        """
        if not (isinstance(duration, float) or isinstance(duration, int)) or duration < 0:
            return False
        if not isinstance(instrument, int) or not 0 <= instrument <= 127:
            return False
        self.player.set_instrument(instrument)
        if not isinstance(octave, int) or octave < 0 or octave > 7:
            return False
        if note is not None:
            if not isinstance(note, str) or note not in self.intervals.keys():
                return False
            self.player.note_on(self.intervals[note] + int(octave) * 12, 120)
            time.sleep(duration)
            self.player.note_off(self.intervals[note] + int(octave) * 12, 120)
            return True
        elif chord is not None:
            if not isinstance(chord, tuple):
                return False
            for chord_note in chord:
                if not isinstance(chord_note, str) or chord_note not in self.intervals.keys():
                    return False
            for chord_note in chord:
                self.player.note_on(self.intervals[chord_note] + octave * 12, 120)
            time.sleep(duration)
            for chord_note in chord:
                self.player.note_off(self.intervals[chord_note] + octave * 12, 120)
            return True
        return False

    def get_melody(self, progression=None, max_notes=50):
        """
            Generate melody for a give chord progression

            Keyword arguments:
                progression -- list of tuples and doubles where each tuple represents a chord and
                    its duration, and doubles represent pauses between chords (default None)
                max_notes -- maximum allowed numbers of notes and pauses in a melody (int > 0, default 20)
            Return:
                list of tuples and doubles, where each tuple contains a note and duration
                    and each double represents a pause
                or False if args have incorrect types or values
        """
        if not (isinstance(progression, list) or isinstance(progression, tuple)):
            return False
        if (not isinstance(max_notes,int)) or max_notes <= 0:
            return False
        melody = []
        number_of_notes_and_pauses = random.randint(1, max_notes)
        round_duration = 0
        chord_timings = []
        chords = []
        for element in progression:
            if isinstance(element, float) or isinstance(element, int):
                round_duration += element
            elif isinstance(element, tuple):
                chord_timings.append([round_duration, round_duration + element[1]])
                chords.append(element[0])
                round_duration += element[1]
        current_duration = 0
        elements = 0
        while current_duration < round_duration and elements < number_of_notes_and_pauses:
            # Add a note or a pause to the melody
            is_note = random.randint(0, 1)
            if is_note == 0:
                dur = rd.uniform(0.0, 2.0, size=1)[0]
                melody.append(dur)
                elements += 1
                current_duration += dur
            else:
                chord = 0
                # Determine currently sounding chord
                while chord < len(chords) - 1:
                    if chord_timings[chord][1] < current_duration < chord_timings[chord + 1][0]:
                        chord += 1
                        break
                    else:
                        chord += 1
                case = random.randint(1, 3)
                root = chords[chord][0]
                # Add root to the melody
                if case == 1:
                    note = root
                # Add the third to the melody
                elif case == 2:
                    note = self.intervals[root] + 5
                    if note >= 12:
                        note -= 12
                    note = self.notes[note]
                # Add the fifth to the melody
                elif case == 3:
                    note = self.intervals[root] + 7
                    if note >= 12:
                        note -= 12
                    note = self.notes[note]
                dur = rd.uniform(0.0, 2.0, size=1)[0]
                current_duration += dur
                elements += 1
                melody.append((note, dur))
        return melody

    def perform(self, to_perform=[], octave=3, instrument=None):
        """
            Play a sequence of notes or chords

            Keyword arguments:
                to_perform -- a list of tuples and doubles where each tuple represents a chord (a note) and
                    its duration, and doubles represent pauses between chords (notes) (default [])
                octave -- integer greater than zero and lesser than 7 representing an octave to play in
                instrument -- integer representing a pygame.midi instrument (default None)
            Return:
                True -- if notes or chords are played successfully
                False -- if args had incorrect types or values
        """
        if not (isinstance(to_perform, list) or isinstance(to_perform, tuple)):
            return False
        for element in to_perform:
            if isinstance(element, int) or isinstance(element, float):
                time.sleep(element)
            else:
                if isinstance(element[0], tuple):
                    self.play(chord=element[0], duration=element[1], octave=octave, instrument=instrument)
                else:
                    self.play(note=element[0], duration=element[1], octave=octave, instrument=instrument)
        return True

    def mix(self, *args, instruments=None):
        """
            Play multiple tracks at once

            Arguments:
                *args -- tracks to be played. Each track is a list or a tuple
                    of notes - capital letters - or chords - tuples of capital
                    letters - and their durations (double numbers), as well as
                    pauses between the sounds - double numbers
            Return:
                True -- if played successfully
                False -- if *args had incorrect types or values
        """
        pos = 0

        for arg in args:
            if isinstance(arg, tuple) or isinstance(arg, list):
                if pos % 2 != 0:
                    return False
                track = arg
                pos += 1
            elif isinstance(arg, int):
                if arg > 7 or arg < 1:
                    return False
                if pos % 2 != 1:
                    return False
                if isinstance(instruments, list) and len(instruments) < int(pos / 2) + 1:
                    return False
                if not isinstance(instruments, int):
                    if not isinstance(instruments[int((pos) / 2)], int):
                        return False
                    elif not 0 <= instruments[int((pos) / 2)] < 80:
                        return False
                    else:
                        ins = instruments[int((pos) / 2)]
                else:
                    if instruments == 0:
                        ins = instruments
                    else:
                        return False

                dir_path = os.path.dirname(os.path.realpath(__file__))
                subprocess.Popen("python \"%s/Generator.py\" \"%s\" %d %d" % (dir_path, track, arg, ins),
                                 shell=True,
                                 stdin=None, stdout=None, stderr=None, close_fds=True)
                pos += 1
                time.sleep(0.1)
            else:
                return False

def main():
    generator = Generator()
    chord_dur = [1, 0.2]
    pause = [0.15, 1]
    progression = [(generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (generator.get_chord('D', 'major'), chord_dur[0]),
                   pause[0],
                   (generator.get_chord('D', 'major'), chord_dur[1]),
                   pause[1],
                   (generator.get_chord('G', 'major'), chord_dur[0]),
                   pause[0],
                   (generator.get_chord('G', 'major'), chord_dur[1]),
                   pause[1],
                   (generator.get_chord('C', 'major'),chord_dur[0]),
                   pause[0],
                   (generator.get_chord('C', 'major'), chord_dur[1]),
                   pause[1],
                   (generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   (generator.get_chord('E', 'minor'), chord_dur[0]),
                   pause[0],
                   (generator.get_chord('E', 'minor'), chord_dur[1]),
                   pause[1],
                   ]
    melody = generator.get_melody(progression, 40)
    generator.mix(progression, 3, melody, 6, instruments=[20,34])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        generator = Generator()
        track = ast.literal_eval(sys.argv[1])
        generator.perform(track, int(sys.argv[2]), int(sys.argv[3]))
    else:
        main()