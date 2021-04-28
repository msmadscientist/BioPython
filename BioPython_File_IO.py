#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:59:08 2021

@author: Kimberly Taylor
Description: Read in fasta file with Biopython
"""

from Bio import SeqIO
from Bio import SeqRecord

folder = "/home/ktaylor/Data/UniProt_04-2021/"
file = folder + "UniProt_Hsapiens+Mmusculus.fasta"
outfile = folder + "UniProt_Kinase_in_Description.fasta"

records = SeqIO.parse(file, "fasta")
# records = list(records)

kinases = []

for record in records:
    if "kinase" in record.description and "inhibitor" not in record.description:
        kinases.append(record)

# for item in kinases:        
out = SeqIO.write(kinases, outfile, "fasta")