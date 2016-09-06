# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 19:58:43 2016

@author: user
"""
from preprocessing import tree_learning_set
from preprocessing import binding_site
from training import nucleotide
from training import finding_index
from test import score_pwm
from test import score_pwm_2
def tree_list():
    X=[]
    Y=[]
    score=score_pwm(tree_learning_set)
    score_2=score_pwm_2(tree_learning_set)
    i=0
    for item in score:
        seq=[]
        for char in item[0]:
            seq.append(finding_index(char,nucleotide))
        seq.append(item[2])
        seq.append(score_2[i][2])
        i+=1        
        X.append(seq)
        Y.append(item[1])
    return [X,Y]
    
from sklearn import tree
clf=tree.DecisionTreeClassifier(min_samples_split=500)
clf=clf.fit(tree_list()[0],tree_list()[1])
from sklearn.externals.six import StringIO
with open("decisionTree.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
