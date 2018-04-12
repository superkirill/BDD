Feature: Testing class Generator

  Scenario: Generate chords
    Given Generator
     When the chord is requested
     Then Generator returns three notes