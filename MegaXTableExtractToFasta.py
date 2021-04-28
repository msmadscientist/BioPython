#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:17:08 2021

@author: Kimberly Taylor
Description: Takes the table-formatted output from a MEGA X tree, extracts
the UniProt sequence names, and matches them to a databases, extracting the
sequences and saving them to fasta file.

"""

import csv
import numpy as np
import re
from Bio import SeqIO

db_folder = "/home/ktaylor/Data/HMM/Results/"
db_file = db_folder + "UniProt_hmm_PK_04-22-2021_KMT.fasta"

table_folder = "/home/ktaylor/Data/HMM/Results/"
table_file = table_folder + "UniProt_hmm_PK_red_04-27-2021_KMT.csv"

out_file = table_folder + "UniProt_hmm_PK_red_04-27-2021_KMT.fasta"

#Open the table and extract sequence names
table = []
with open(table_file, "r") as infile:
    csvread = csv.reader(infile, delimiter = ",")
    for row in csvread:
        table.append(row)
        
table = np.array(table)

sequence_names = []

for i in range(np.shape(table)[0]):
    for j in range(np.shape(table)[1]):
        if re.search(" sp\\|[A-Z0-9]+",table[i][j]):
            sequence_names.append(table[i][j][1:]) #Remove initial space

codes = []
#Massage sequence names to get just the UniProt codes
for name in sequence_names:
    match = re.search("sp\\|[A-Z0-9]+\\|", name)
    codes.append(match[0][3:-1])
      
#Open the database
db = list(SeqIO.parse(db_file, "fasta"))

#Extract sequences from the database
sequences = []

for item in db:
    for code in codes:
        if code in item.description:
            sequences.append(item)
            
#Write sequences to fasta file
out = SeqIO.write(sequences, out_file, "fasta")