import musicpy as mp

# Vars
sentence = "(1/8-1/8 A4-C4-E4),(1/4 A4-C4-F4),(1/3-1/5 A5-D5)"
stripped_sentence = sentence.replace('(',"").replace(')',"")
words = stripped_sentence.split(',')
rhythms = []
notes = []
# Print
print("Sentence:", sentence)
print("Words:", words)
print()
for i in range(len(words)):
    # Vars
    rhythms = words[i].split(' ')[0].split('-')
    notes = words[i].split(' ')[1].split('-')
    # Print
    print("##", words[i], "##")
    print("Rhythms:", rhythms)
    print("Notes:", notes)
    print()
    # Sound
    mp.chord(notes, rhythms)