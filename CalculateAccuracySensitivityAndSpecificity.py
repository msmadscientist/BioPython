 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 23:37:58 2021

@author: Kimberly Taylor
Description: Calculates accuracy, specificity, and sensitivity
"""

import csv
import math
import pandas as pd
import numpy as np

folder = "/home/ktaylor/Data/HMM/Results/"
file = folder + "UniProt_Dualhmm_SVM.csv"

def calculate_TP_TN_FP_FN (data, P, F):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(data)):
        if data['Prediction'][i] == P and data['Actual'][i] == P:
            TP += 1
        elif data['Prediction'][i] == F and data['Actual'][i] == F:
            TN += 1
        elif data['Prediction'][i] == F and data['Actual'][i] == P:
            FN += 1
        elif data['Prediction'][i] == P and data['Actual'][i] == F:
            FP += 1
    return TP, TN, FP, FN

def calculate_accuracy (TP, TN, FN, FP):
    return (TP+TN)/(TP+TN+FN+FP)

def calculate_sensitivity (TP, TN, FN, FP):
    return TP/(TP+FN)

def calculate_specificity (TP, TN, FN, FP):
    return TN/(TN+FP)


db = pd.read_csv(file)

P = "S"
F = "T"

TP, TN, FP, FN = calculate_TP_TN_FP_FN(db, P, F)

accuracy = calculate_accuracy(TP, TN, FP, FN)*100
sensitivity = calculate_sensitivity(TP, TN, FN, FP)*100
specificity = calculate_specificity(TP, TN, FN, FP)*100

print("Positive %s, negative %s" % (P, F))
print ("Accuracy %.2f" % (accuracy))
print ("Sensitivity %.2f" % (sensitivity))
print ("Specificity %.2f" % (specificity ))

P = "T"
F = "S"

TP, TN, FP, FN = calculate_TP_TN_FP_FN(db, P, F)

accuracy = calculate_accuracy(TP, TN, FP, FN)*100
sensitivity = calculate_sensitivity(TP, TN, FN, FP)*100
specificity = calculate_specificity(TP, TN, FN, FP)*100

print("Positive %s, negative %s" % (P, F))
print ("Accuracy %.2f" % (accuracy))
print ("Sensitivity %.2f" % (sensitivity))
print ("Specificity %.2f" % (specificity ))