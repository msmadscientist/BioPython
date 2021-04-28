#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 23:12:37 2021

@author: Kimberly Taylor
Description: Runs Clustal Omega alignment using Python
"""

import os
from Bio import SeqIO
from Bio import AlignIO
from subprocess import *
from Bio.Align.Applications import ClustalOmegaCommandline

folder = "/home/ktaylor/Data/HMM/Models/"
unaligned = folder + "P09619_BLAST_top50_04-26-2021_KMT.fasta"
aligned = folder + "P09619_BLAST_top50_04-28-2021_KMT_clustalo.fasta"

clustalo_exe = "/usr/bin/clustalo"

# records = SeqIO.parse(unaligned, "fasta")

clustalo_align = ClustalOmegaCommandline(clustalo_exe, infile = unaligned, outfile = aligned, 
                                         outfmt = "fasta", verbose = True, auto = True)

stdout, stderr = clustalo_align()