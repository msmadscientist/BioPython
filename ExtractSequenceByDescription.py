#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:17:50 2021

@author: ktaylor
"""

from Bio import SeqIO
import numpy as np

folder = "/home/ktaylor/Data/HMM/Results/"
file = folder + "UniProt_hmm_PK_04-22-2021_KMT.fasta"
SerThr_file = folder + "UniProt_hmm_PK_04-22-2021_KMT_SerThr.fasta"
Tyr_file = folder + "UniProt_hmm_PK_04-22-2021_KMT_Tyr.fasta"
Dual_file = folder + "UniProt_hmm_PK_04-22-2021_KMT_Dual.fasta"

all_sequences = SeqIO.parse(file, "fasta")

SerThr_sequences = []
Tyr_sequences = []
Dual_sequences = []

for sequence in all_sequences:
    if "Serine/threonine" in sequence.description or "serine/threonine" in sequence.description:
        SerThr_sequences.append(sequence)
    elif "Tyrosine" in sequence.description or "tyrosine" in sequence.description:
        Tyr_sequences.append(sequence)
    elif "Dual" in sequence.description or "dual" in sequence.description:
        Dual_sequences.append(sequence)
        
SerThr_out = SeqIO.write(SerThr_sequences, SerThr_file, "fasta")
Tyr_out = SeqIO.write(Tyr_sequences, Tyr_file, "fasta")
Dual_out = SeqIO.write(Dual_sequences, Dual_file, "fasta")