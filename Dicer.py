import numpy as np
from random import randint

def create_fragments(sequence):
    siRNA = []
    rnas = round(len(sequence)/25)
    for _ in range(rnas):
        start = randint(0,len(sequence)-25)
        end = start+randint(20,25)
        siRNA.append(sequence[start:end])
    return siRNA

seq = input('Paste sequence here: \n')
fragments = create_fragments(seq)

fragments = np.unique(fragments)

with open('output.txt','w') as file:
    for i, f in enumerate(fragments):
        file.write(f">fragment {i}\n")
        file.write(f"{f}\n")