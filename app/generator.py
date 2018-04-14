import pygame.midi
import time

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
        self.player.set_instrument(instrument)
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
