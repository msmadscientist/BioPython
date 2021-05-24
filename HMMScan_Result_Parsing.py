#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:00:36 2021

@author: Kimberly Taylor
Description: Reads in output file from hmmscan and parses results,
outputting results to fasta file of sequences with evalues < minimum and
output file.
"""

import csv
from collections import defaultdict
from Bio import SeqIO
from Bio import SearchIO

hmmer_folder = "/home/ktaylor/Data/HMM/Results/"
hmmer_file = hmmer_folder + "UniProt_hmm_PK_PK-Two_Kinase_05-02-2021_KMT.out"

db_folder = "/home/ktaylor/Data/HMM/Results/"
db_file = db_folder + "UniProt_hmm_PK_04-22-2021_KMT.fasta"

hmmer_output_file = hmmer_folder + "UniProt_hmm_PK_PK-Two_Kinase_05-02-2021_KMT.csv"
fasta_output_file = hmmer_folder + "UniProt_hmm_PK_PK-Two_Kinase_05-02-2021_KMT.fasta"

evalue_cutoff = 1e-3

#Read in results from hmmsearch output
hmmsearch_output = list(SearchIO.parse(hmmer_file, "hmmscan3-domtab"))

#Find HMMs used for hmmsearch
hmms = []

for search in hmmsearch_output:
    for query in search:
        if query.id not in hmms:
            hmms.append(query.id)

#Read evalues for these hmms into a dictionary based on search ids.  Note:
#this only reads in the second value for the evalue, if there are two.
all_ids = {}
for search in hmmsearch_output:
    for query in search:
        for hit in query:
            if hit.evalue < evalue_cutoff:
                if search.id in all_ids.keys():
                    all_ids[search.id][query.id] = hit.evalue
                else:
                    all_ids[search.id] = {query.id: hit.evalue}

#Read in database using BioPython SeqIO
db = list(SeqIO.parse(db_file, "fasta"))

#Get sequences that match ids from hmmsearch results
all_sequences = []
for id in all_ids:
    for query in search:
        for n in range(len(db)):
            if db[n].id == id:
                all_sequences.append(db[n])
                all_ids[id]['description'] = db[n].description
                continue
        

                    
#Output ids and evalues to csv file
with open(hmmer_output_file, "w") as outfile:
    csvwrite = csv.writer(outfile,delimiter = ",")
    csvwrite.writerow(["ID, Description, HMM, E-Value"])
    for key in all_ids:
        csvwrite.writerow([key,all_ids[key]['description'], hmms[0], all_ids[key][hmms[0]], hmms[1], all_ids[key][hmms[1]]])
    
#Output sequences that passed hmmsearch
output = SeqIO.write(all_sequences, fasta_output_file, "fasta")