#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:11:48 2021

@author: ktaylor
"""

from Bio import SeqIO

folder = "/home/ktaylor/Data/HMM/Results/"
file = folder + "UniProt_hmm_PK_04-22-2021_KMT_SerThr_mafft.fasta"
output = file[:-5] + "so"

sequences = SeqIO.parse(file, "fasta")

out = SeqIO.write(sequences, output, "stockholm") 