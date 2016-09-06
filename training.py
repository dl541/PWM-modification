# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 09:17:36 2016

@author: user
"""
import numpy as np
import math
import preprocessing as prep
np.set_printoptions(precision=4)

bases=["A","C","G","T"]
nucleotide={}
num=0
for i in range(4):
    nucleotide.update({i:bases[i]})
    num+=1

dinucleotide={}
num=0
for i in range(4):
    for j in range(4):
        dinucleotide.update({num:nucleotide[i]+nucleotide[j]})
        num+=1
        
def finding_index(char,dictionary):
    for key in dictionary:
        if dictionary[key]==char:
            return key
        

"""with open("training_set.txt","r") as f:
    bad_char=["a","t","c","g"," ","\n"]
    i=0
    prep.binding_site=[]
    for line in f:
        if i%2==0:            
            text=""
            for char in line:
                if char not in bad_char:
                    text=text+char
            if text!="":
                prep.binding_site.append(text)
        elif text!="":
            frequency=int(line)
            for num in range(frequency-1):
                prep.binding_site.append(text)
        i+=1
print prep.binding_site"""
            
pfm=np.array([[0.0]*len(prep.binding_site[0])]*len(nucleotide))

for element in prep.binding_site:
    i=0
    for char in element:
        pfm[finding_index(char,nucleotide)][i]+=1
        i+=1
total_sample=np.sum(pfm,axis=0)[0]
#pseudocount
pfm=np.clip(pfm,1.0,total_sample)
       
#print "pfm: "
#print pfm
#print "\n"

ppm=pfm/total_sample
#print "ppm: "
#print ppm
#print "\n"

pwm=ppm

pwm=np.log(ppm/0.25)/math.log(2)
#print "pwm: "
#print pwm
#print "\n"

pfm_2=np.array([[0.0]*(len(prep.binding_site[0])-1)]*len(dinucleotide))
for element in prep.binding_site:
    for index in range(len(element)-1):
        pfm_2[finding_index(element[index]+element[index+1],dinucleotide)][index]+=1

total_sample=np.sum(pfm_2,axis=0)[0]
#pseudocount
pfm_2=np.clip(pfm_2,1.0,total_sample)
#print "pfm_2"
#print pfm_2
#print "\n"
ppm_2=pfm_2/total_sample
#print "ppm_2: "
#print ppm_2
#print "\n"

pwm_2=ppm_2

pwm_2=np.log(ppm_2/(0.25**2)/math.log(2))

#print "pwm_2"
#print pwm_2

"""site_length=len(pwm[0])
pfm_2=np.array([[0]*(site_length*site_length)]*16)

for element in binding_site:
    i=0
    j=0
    for i in range(len(element)):
        for j in range(len(element)):
            #print pfm_2
            if i==j:
                pfm_2[i][j]=0
            else:
                pfm_2[finding_index(element[i]+element[j],dinucleotide)][int(str(i)+str(j),len(element))]+=1
        
np.savetxt("pfm_2.txt",pfm_2,fmt='%1.0f')"""
