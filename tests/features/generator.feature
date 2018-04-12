Feature: Testing class Generator

  Scenario Outline: Generate chord
    Given Generator
     When the chord <chord> is requested
     Then Generator returns <notes>

    Examples: Chords
    | chord      | notes      |
    | A          | A, C#, E   |
    | A#         | A#, D, F   |
    | B          | B, D#, F#  |
    | C          | C, E, G    |
    | C#         | C#, F, G#  |
    | D          | D, F#, A   |
    | D#         | D#, G, A#  |
    | E          | E, G#, B   |
    | F          | F, A, C    |
    | F#         | F#, A#, C# |
    | G          | G, B, D    |
    | G#         | G#, C, D#  |
    | A, minor   | A, C, E    |
    | A#, minor  | A#, C#, F  |
    | B, minor   | B, D, F#   |
    | C, minor   | C, D#, G   |
    | C#, minor  | C#, E, G#  |
    | D, minor   | D, F, A    |
    | D#, minor  | D#, F#, A# |
    | E, minor   | E, G, B    |
    | F, minor   | F, G#, C   |
    | F#, minor  | F#, A, C#  |
    | G, minor   | G, A#, D   |
    | G#, minor  | G#, B, D#  |


  Scenario Outline: Generate bad chord
    Given Generator
    When the wrong chord <bad_chord> is requested
    Then Generator throws a ValueError

    Examples: Bad Chords
    | bad_chord      |
    | G#, superchord |
    | XYZ            |
    | 214`e23f       |
    | SOSISKI ALTAYA |