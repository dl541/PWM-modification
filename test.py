# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 10:52:27 2016

@author: user
"""
import matplotlib.pyplot as plt

import training as train
import preprocessing as prep


def score_pwm(evaluating_set):
    result_list=[]
    with open("result_pwm.txt","w") as result:
        for element in evaluating_set:
            for i in range(len(element)-len(train.pwm[0])+1):
                score=0.0
                seq=element[i:(i+len(train.pwm[0]))]
                clf=(seq.upper()==seq)
                seq=seq.upper()
                for j in range(len(seq)):
                    score=score+train.pwm[train.finding_index(seq[j],train.nucleotide)][j]
                result_list.append([seq,clf,score])    
                result.write(seq+"   "+str(clf)+"   "+str(score)+"\n")
    return result_list

def performance(lst,threshold):
    #print "testing_set_size: "+str(len(lst))
    TP=0.0
    TN=0.0
    FP=0.0
    FN=0.0    
    for item in lst:
        if item[1]:
            if item[2]>=threshold:
                TP+=1
            else:
                FN+=1
        else:
            if item[2]<=threshold:
                TN+=1
            else:
                FP+=1
    sensitivity=TP/(TP+FN)
    specificity=TN/(TN+FP)
    #print sensitivity
    #print specificity
    return [sensitivity,specificity]    
    
def score_pwm_2(evaluating_list):
    result_list=[]
    with open("result_pwm_2.txt","w") as result:
        for element in evaluating_list:
            for i in range(len(element)-len(train.pwm[0])+1):
                score=0.0
                seq=element[i:(i+len(prep.binding_site[0]))]
                clf=(seq.upper()==seq)
                seq=seq.upper()
                for j in range(len(seq)-1):
                    score=score+train.pwm_2[train.finding_index(seq[j]+seq[j+1],train.dinucleotide)][j]
                result_list.append([seq,clf,score])    
                result.write(seq+"   "+str(clf)+"   "+str(score)+"\n")
    return result_list

def AUC_graph(lst,threshold_lst):
    x=[]
    y=[]
    for num in threshold_lst:
        y.append(performance(lst,num)[0])
        x.append(1-performance(lst,num)[1])
          
    plt.plot(x,y,'ro')
    plt.axis([0, 1, 0, 1])    
    

