# Music Generation with music21

This Python script utilizes the `music21` library to generate a simple melody in the key of C major and saves it as a MIDI file. The generated melody consists of the notes C4, D4, E4, F4, G4, A4, B4, and C5, each with a duration of 1.0 beat.

## Dependencies
- [music21](http://web.mit.edu/music21/)

## How to Run
1. Install the `music21` library by running:
    ```bash
    pip install music21
    ```

2. Run the script:
    ```bash
    python your_script_name.py
    ```

## Output
After running the script, a MIDI file named `generated_music.mid` will be created in the same directory. This MIDI file represents the generated melody.

## Customization
Feel free to modify the `pitches_collection` and `durations_data` lists to create different melodies. You can refer to the [music21 documentation](http://web.mit.edu/music21/doc/index.html) for more options and features.

## Note
Ensure that you have a MIDI player or a music software to play the generated MIDI file.

---

**Note:** Include relevant links and adjust the file names as necessary.
