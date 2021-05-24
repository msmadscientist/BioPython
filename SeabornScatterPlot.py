#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 23:37:39 2021

@author: ktaylor
"""

import csv
import math
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

folder = "/home/ktaylor/Data/HMM/Results/"
file = folder + "UniProt_Dualhmm_TrainingSet.csv"

db = pd.read_csv(file)

sns.color_palette("Spectral", as_cmap=True)
splot = sns.scatterplot(data = db, x = db["Pkinase Evalue"], y = db["PK_Tyr_Ser-Thr Evalue"], hue = db["Type"])
splot.set(xscale = "log", yscale = "log")
