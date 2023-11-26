import json
from mido import Message, MidiFile, MidiTrack

# Function to read river data from a file
def read_river_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Convert river data to MIDI control changes
def river_data_to_midi(river_data, control_number):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    for data_point in river_data:
        control_value = int(data_point['flow_rate']) % 127  # Scale as needed
        track.append(Message('control_change', control=control_number, value=control_value, time=0))

    return midi

# Main function
def main():
    locations = ['Mountain', 'Valley', 'Ocean']
    control_numbers = {'Mountain': 1, 'Valley': 2, 'Ocean': 3}  # Assign different control numbers for each location

    for location in locations:
        file_path = f"{location}_data.json"
        river_data = read_river_data(file_path)
        midi = river_data_to_midi(river_data, control_numbers[location])

        with open(f"{location}_river_data.mid", "wb") as output_file:
            # Save the MIDI file
            midi_file_path = f"{location}_river_data.mid"
            midi.save(midi_file_path)

if __name__ == "__main__":
    main()
