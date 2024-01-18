import music21

# create a stream object to hold the music data
melody_data = music21.stream.Stream()

# add a key signature of C major to the melody_data
melody_data.append(music21.key.Key('C'))

# define a list of pitches for the melody
pitches_collection = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# define a list of durations for the melody
durations_data = [music21.duration.Duration(1.0)] * len(pitches_collection)

# create a list of notes by pairing the pitches and durations
list_notes = [music21.note.Note(pitch, duration=dur) for pitch, dur in zip(pitches_collection, durations_data)]

# add the notes to the melody stream
for note in list_notes:
    melody_data.append(note)

# save the music to a MIDI file
melody_data.write('midi', fp='generated_music.mid')
print("The music has been successfully generated")