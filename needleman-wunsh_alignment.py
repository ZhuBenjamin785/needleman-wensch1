import random
import numpy as np

Nucleotides = ["A", "C", "G", "T",]

def validateSeq (dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return True    


def Length(dna_seq, length):
    length = len(dna_seq)
    return length
        

def backtrack(matrix, sequence1, sequence2, matchValue, mismatchPen, gapPen):
    counter1 = len(sequence1)
    counter2 = len(sequence2)
    aligned1 = []
    aligned2 = []

    while counter1 > 0 or counter2 > 0:
        current = matrix[counter1][counter2]
        if counter1 > 0 and counter2 > 0:
            diagonalScore = matrix[counter1 - 1][counter2 - 1]
            expected = match(sequence1[counter1 - 1], sequence2[counter2 - 1], diagonalScore, matchValue, mismatchPen)
            
            if current == expected:
                aligned1.append(sequence1[counter1 - 1])
                aligned2.append(sequence2[counter2 - 1])
                counter1 -= 1
                counter2 -= 1
                continue
        if counter1 > 0 and current == matrix[counter1 - 1][counter2] - gapPen:
            aligned1.append(sequence1[counter1 - 1])
            aligned2.append("-")
            counter1 -= 1
        else:
            aligned1.append("-")
            aligned2.append(sequence2[counter2 - 1])
            counter2 -= 1

    return "".join(aligned1), "".join(aligned2)
            
        

def topGapPenalty(value1, gapPen):
    return value1 - gapPen
 
def leftGapPenalty(value1, gapPen):
    return value1 - gapPen
 
def match (letter1, letter2, value, matchValue, mismatchPen):
    if letter1 == letter2:
        return value + matchValue
    else:
        return value - mismatchPen




rndDNAStr = input("enter a nucleotide sequence: ")
while validateSeq (rndDNAStr) == False:
    rndDNAStr = input("Enter valid sequence: ")

rndDNAStr2 = input("enter  a nucleotide sequence 2: ")
while validateSeq(rndDNAStr2) == False:
    rndDNAStr2 = input("Enter valid sequence: ")

length1 = 0
length1 = Length(rndDNAStr, length1)
length2 = 0
length2 = Length(rndDNAStr2, length2)


matchValue = int(input("enter a match value: "))
mismatchPen = int(input("enter a mismatch penalty (positive, will be negated automatically): "))
gapPen = int(input("enter a gap penalty (positive, will be negated automatically): "))



matrix = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]
for matrix1, nuc in enumerate(rndDNAStr):
    matrix[matrix1 + 1][0] = (matrix1 + 1) * -gapPen


for matrix2, nuc1 in enumerate(rndDNAStr2):
    matrix[0][matrix2 + 1] = (matrix2 + 1) * -gapPen

for matrix1 in range(1, length1 + 1):
    for matrix2 in range(1, length2 + 1):
        letterA = rndDNAStr[matrix1 - 1]
        letterB = rndDNAStr2[matrix2 - 1]
 
        value3 = matrix[matrix1 - 1][matrix2 - 1]  
        value2 = matrix[matrix1 - 1][matrix2]       
        value1 = matrix[matrix1][matrix2 - 1]       
 
        diagonal = match(letterA, letterB, value3, matchValue, mismatchPen)
        up = topGapPenalty(value2, gapPen)
        left = leftGapPenalty(value1, gapPen)
 
        matrix[matrix1][matrix2] = max(diagonal, up, left)

print()
for row in matrix:
    print(row)
print()


revAligned1, revAligned2 = backtrack(matrix, rndDNAStr, rndDNAStr2, matchValue, mismatchPen, gapPen)

aligned1 = revAligned1[::-1]
aligned2 = revAligned2[::-1]
print("alignment:")
print(aligned1)
print(aligned2)
print("AlignmentScore:", matrix[length1][length2])



 
