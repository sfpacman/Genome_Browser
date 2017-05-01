#!/usr/bin/python
from Bio.Restriction import BamHI
from Bio.Restriction import EcoRI
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
amb = IUPACAmbiguousDNA()

def find_BamHi (DNA_sequence):
    "Find BamHi restriction site and give position of sticky ends"
    pos=[] 
    bam_start= BamHi.search(DNA_sequence)
    for entry in bam_start:
        bam_end = entry + 4
        bam.append(entry)
        pos.append(bam_end)
    return(pos);

import re
def find_BsuMi (DNA_sequence):
    "Find BsuMi restriction site and give position on the cut"
    bsumi = re.search(r"CTCGAG", DNA_sequence)
    #start of the recognition site on the sequence
    bsu_start = bsumi.start()
    #cut of the enzyme on the sequence
    bsu_cut = bsu_start + 3
    return(bsu_cut);

def find_EcoRi (DNA_sequence):
    "Find EcoRi restriction site and give position of sticky ends"
    pos=[]
    eco_start= EcoRI.search(DNA_sequence)
    for entry in eco_start:
        eco_end = entry + 4
        pos.append(entry)
        pos.append(eco_end)
    return(pos);

