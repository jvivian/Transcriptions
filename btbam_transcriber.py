#!/usr/bin/env python2.7
# John Vivian
"""
Script to transcribe BTBAM tabs in drop tuning

User input:  <string>-<fret> 
Response:  Note
"""

def print_note(string, fret):
    print '\n{}\n'.format(strings[string-1][fret])

s1 = ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'] * 3
s2 = ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F'] * 3
s3 = ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'] * 3
s4 = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'] * 3
s5 = ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'] * 3
strings = [s1, s2, s3, s4, s5, s1]

while True:
    inp = raw_input("Enter <string>-<fret>, (x to exit): ")
    if inp == 'x' or inp == 'X':
        break
    string, fret = inp.split('-')
    print_note(int(string), int(fret))
    

