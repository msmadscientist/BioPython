#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:24:42 2021

@author: Kimberly Taylor
Description: Parses outfile from HMMsearch, extracting full sequences
from an indicated fasta database and writing out an output file.
"""

import csv
from Bio import SeqIO
from Bio import SearchIO

hmmer_folder = "/home/ktaylor/Data/HMM/Results/"
hmmer_file = hmmer_folder + "UniProt_hmm_PK_04-22-2021_KMT.out"

db_folder = "/home/ktaylor/Data/UniProt_04-2021/"
db_file = db_folder + "UniProt_Hsapiens+Mmusculus.fasta"

hmmer_output_file = hmmer_folder + "UniProt_hmm_PK_04-22-2021_KMT.csv"
fasta_output_file = hmmer_folder + "UniProt_hmm_PK_04-22-2021_KMT.fasta"

evalue_cutoff = 1e-3

#Read in results from hmmsearch output
hmmsearch_output = SearchIO.read(hmmer_file, "hmmer3-text")

#Parse through hmmsearch output, rejecting entries that have high
#e-values
names = []
evalues = []

for entry in hmmsearch_output:
    if len(entry) == 1:
        if entry[0].evalue < evalue_cutoff:
            names.append([entry.id, entry.description])
            evalues.append([entry[0].evalue, entry[0].hit_range])
    else:
        if entry[0].evalue < evalue_cutoff and entry[1].evalue < evalue_cutoff:
            names.append([entry.id, entry.description])
            evalues.append([entry[0].evalue, entry[0].hit_range, entry[1].evalue, entry[1].hit_range])                           

#Write data to csv file
with open(hmmer_output_file,'w') as outfile:
    outwriter = csv.writer(outfile, delimiter=',')
    outwriter.writerow(["Protein name, Description, E-Value, Match Begin, Match End, E-Value, Match Begin, Match End"])
    for i in range(len(names)):
        outwriter.writerow([names[i],evalues[i]])
        
#Using names array, collect complete sequences of all matches from database
#specified
db = SeqIO.parse(db_file, "fasta")
full_seqs = []

for item in db:
    for n in range(len(names)):
        if item.id in names[n]:
            full_seqs.append(item)
            
out = SeqIO.write(full_seqs,fasta_output_file, "fasta")