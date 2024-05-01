from music21 import *
from PIL import Image, ImageDraw

#Parse the midi file
def parse_midi(file_path):
    midi = converter.parse(file_path)
    return midi

# Note to color mapping
note_colors = {
    "C": "#FF0000",
    "D": "#FFA500",
    "E": "#FFFF00",
    "F": "#008000",
    "G": "#0000FF",
    "A": "#4B0082",
    "B": "#EE82EE",
    "C#": "#FF6347",
    "D#": "#FFD700",
    "F#": "#00FF00",
    "G#": "#1E90FF",
    "A#": "#800080"
}

# Draw the image
def draw_image(notes, file_path):

    max_width = 1000
    max_height = 1000

    width_per_note = max_width / len(notes.recurse().notesAndRests)
    note_width = max(20, width_per_note * 0.8)
    spacing = width_per_note  * 0.2


    img = Image.new('RGB', (1000, 1000), color = 'white')
    draw = ImageDraw.Draw(img)
    x = 0
    y = 0
    for item in notes.recurse().notesAndRests:
        if item.isNote:
            color = note_colors.get(item.name, '#000000')
            draw.rectangle([x, 50, x + note_width, 100], fill=color)
            x += width_per_note
        elif item.isChord:
            # Using the root note of the chord for color
            root_note = item.root().name
            color = note_colors.get(root_note, '#000000')
            draw.rectangle([x, 50, x + note_width, 100], fill=color)
            x += width_per_note
    img.save(file_path)

# Main function
def main():
    notes = parse_midi("../MIDI/Hungarian-Rhapsody-Nr-2.mid")
    draw_image(notes, "test.png")

if __name__ == "__main__":
    main()
