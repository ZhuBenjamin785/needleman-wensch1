Nucleotides = ["A", "C", "G", "T",]
def validateSeq (dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq
    
def countNucFrequency (seq):
    tmpFreqDict = {"A": 0, "C": 0, "G":0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict



def transcription(seq):
    return seq.replace("T" , "U")

def gappingSystem (seq):
    tmpOrder = 0
    nucOrder = 0
    for nuc in seq:
        tmpOrder += 1
        nucOrder = tmpOrder
        nucOrder *= -2
        print (nuc, nucOrder)
        

def transcription(seq):
    return seq.replace("T", "U")
 
def topGapPenalty(value1):
    return value1 - 2
 
def leftGapPenalty(value1):
    return value1 - 2
 
def match (letter1, letter2, value):
    if letter1 == letter2:
        return value + 1
    else:
        return value - 1