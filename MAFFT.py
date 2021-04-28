#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:40:23 2021

@author: Kimberly Taylor
Description: MAFFT alignment using BioPython
"""

from Bio import AlignIO
from io import StringIO
from Bio.Align.Applications import MafftCommandline

folder = "/home/ktaylor/Data/HMM/Models/"
unaligned = folder + "P09619_BLAST_top50_04-26-2021_KMT.fasta"
aligned = folder + "P09619_BLAST_top50_04-28-2021_KMT_mafft.fasta"

mafft_exe = "/usr/bin/mafft"

mafft_cline = MafftCommandline(mafft_exe,input = unaligned)

stdout, stderr = mafft_cline()

aligned_sequences = AlignIO.read(StringIO(stdout), "fasta")

out = AlignIO.write(aligned_sequences, aligned, "fasta")

# stdout, stderr = mafft_cline()

# with open(aligned, "w") as handle:
#     handle.write(stdout)

# align = AlignIO.read(mafft, "fasta")

# mafft = AlignIO.parse(open(mafft), "fasta")

# for record in mafft:
#     print(record.seq + " " + record.id)
# # out = AlignIO.write(mafft, aligned, "fasta")