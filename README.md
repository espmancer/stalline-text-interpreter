# stalline-text-interpreter
Reads, filters, and plays customized musical notation for a fictional language I'm working on. In a worldbuilding sense, this is primarily used when it's more efficient or convienent to write than musical notation.
## Rules
The standard reading is in the C Major key at 120 bpm where the beat is carried by a quarter note.
### Words
- Every word is grouped by parenthesis (this is more for readability)
- Words are seperated by commas
- Each property of the word is divided by a space
### Rhythms
- Rhythms are indicated by a fraction
- Multiple rhythms are connected by a dash (-)
### Notes 
- Notes are indicated by a letter and its octave
- Multiple notes are connected by a dash (-)
## Example
### Sentence
(1/8-1/8 C3-E3-G3),(1/4-1/8 C3-F3-A3),(1/4 B3-F3-G3),(1/2-1/2 C3-E3-G3)
### Words
**(1/8-1/8 C3-E3-G3)**  
Rhythm: Two 8th notes  
Notes: C3, E3, and G3  
**(1/4-1/8 C3-F3-A3)**  
Rhythm: One quarter note and one 8th note  
Notes: C3, F3, A3  
**(1/4 B3-F3-G3)**  
Rhythm: One quarter note  
Notes: B3, F3, G3  
**(1/2-1/2 C3-E3-G3)**  
Rhythm: 2 half notes  
Notes: C3, E3, G3
