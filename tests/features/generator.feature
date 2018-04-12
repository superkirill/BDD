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