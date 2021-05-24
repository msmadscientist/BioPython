#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:12:33 2021

@author: ktaylor
"""

import csv
import math
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

hmmer_folder = "/home/ktaylor/Data/HMM/Results/"

ratios_file = hmmer_folder + "S_and_T_Ratios_Training_Set_05-07-2021.csv"
dual_file = hmmer_folder + "Dual_Ratios_Training_Set_05-07-2021.csv"
ratios = pd.read_csv(ratios_file)
dual = pd.read_csv(dual_file)


ax = sns.kdeplot(data = ratios['Serine-Threonine'], shade = True, color = "b")
ax = sns.kdeplot(data = ratios['Tyrosine'], shade = True, color = "r")
ax = sns.kdeplot(data = dual, shade = True, color = "g")
ax.set_xlabel("Log10(Ratio of E-values of PKinase to P_Ser_Thr_Tyr)")
ax.set_ylabel("Density")
ax.legend(["Serine//Threonine", "Tyrosine", "Dual"], loc = "upper left")
# plt.show()