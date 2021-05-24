#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:03:48 2021

@author: Kimberly Taylor
Description: SVM for two categories using scikit-learn
Plot from https://chrisalbon.com/machine_learning/support_vector_machines/plot_support_vector_classifier_hyperplane/
"""

import csv
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm, datasets
from sklearn.metrics import accuracy_score

folder = "/home/ktaylor/Data/HMM/Results/"
training_file = folder + "UniProt_Dualhmm_TrainingSet_Two_Types.csv"
testing_file = folder + "UniProt_Dualhmm_TestingSet.csv"
out_file = folder + "UniProt_Dualhmm_SVM.csv"

training = pd.read_csv(training_file)
testing = pd.read_csv(testing_file)

X = []
#Create array of values for testing
for i in range(len(training["Pkinase Log(Evalue)"])):
    row = [training["Pkinase Log(Evalue)"][i],training["PK_Tyr_Ser-Thr Log(Evalue)"][i]]
    X.append(row)
    
testingX = []

for i in range(len(testing["Pkinase Log(Evalue)"])):
    row = [testing["Pkinase Log(Evalue)"][i],testing["PK_Tyr_Ser-Thr Log(Evalue)"][i]]
    testingX.append(row)
    
X = np.array(X)
testingX = np.array(testingX)
y = np.array(training["Type"])

colors = {"Serine-Threonine": "red", "Tyrosine": "blue"}
clf = svm.SVC(kernel = "linear")
clf.fit(X,y)
fit = clf.fit(X,y)
coef = clf.coef_
intercept = clf.intercept_
minx = np.min(X[:,0])-1
maxx = np.max(X[:,1])+1
xx = np.linspace(minx, maxx)
a = -coef[0][0]/coef[0][1]
yy = a * xx - (intercept[0])/coef[0][1]


fig, ax = plt.subplots()
ax.scatter(X[:,0],X[:,1], c = training["Type"].map(colors))
ax.plot(xx,yy, c = "black", linestyle = "-")
plt.xlabel("Pkinase log(evalue)")
plt.ylabel("PK_Tyr_Ser-Thr log(evalue)")
# plt.legend(["Serine-Threonine", "Tyrosine"])
plt.show()

prediction = clf.predict(testingX)

colors = {"S": "red", "T": "blue", "D": "green", "U": "orange", "N": "yellow"}
fig2, ax2 = plt.subplots()
ax2.scatter(testingX[:,0],testingX[:,1], c = testing["Actual"].map(colors))
ax2.plot(xx,yy, c = "black", linestyle = "-")
plt.xlabel("Pkinase log(evalue)")
plt.ylabel("PK_Tyr_Ser-Thr log(evalue)")
# plt.legend(["Serine-Threonine", "Tyrosine"])
plt.show()

#Get one-letter abbreviations for the two kinase types
predicted = []

for item in prediction:
    predicted.append(item[:1])
    
actual = testing["Actual"]

#Output results

print("Accuracy %.2f" % (accuracy_score(actual, predicted)*100))
print("Classes:")
print(clf.classes_)
print("Coefficients:")
print(clf.coef_)
print("Intercepts:")
print(clf.intercept_)

#Put actual and predicted together into the array data
data = []

for n in range(len(predicted)):
    row = [actual[n], predicted[n]]
    data.append(row)
    
data = np.array(data)

#Create new data frame and write to file
df = pd.DataFrame(data, columns = ["Actual", "Prediction"])

df.to_csv(out_file)