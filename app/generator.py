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

    def get_chord(self, root='C'):
        """
            Generate a chord

            Keyword arguments:
                root -- capital letter from A to G, (default 'C')
            Return:
                tuple of three notes the chord consists of, e.g. ('C', 'E', 'G')
        """
        third = self.intervals[root] + 4
        if third >= 12:
            third -= 12
        third = self.notes[third]
        fifth = self.intervals[root] + 7
        if fifth >= 12:
            fifth -= 12
        fifth = self.notes[fifth]
        return (root, third, fifth)