# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 11:02:16 2016

@author: user
"""
#counting number of lines in raw_data
line_number=0
with open("raw_data.txt","r") as f:
    for line in f:
        line_number+=1
        
total_line_number=line_number

#spliting raw_data into testing_set, training_set
line_number=0
with open("raw_data.txt","r") as f:
    with open("training_set.txt","w") as training_set:
        with open("testing_set.txt","w") as testing_set:
            split=False
            for line in f:
                line_number+=1
                
                if line_number<=total_line_number/2:
                    training_set.write(line)
                else:
                    if split==False:
                        if list(set(list(line))&set( ["a","t","c","g","A","T","C","G"]))==[]:
                            training_set.write(line)
                        else:
                            split=True
                            testing_set.write(line)
                    else:
                        testing_set.write(line)
            
with open("training_set.txt","r") as f:
    bad_char=["a","t","c","g"," ","\n"]
    i=0
    binding_site=[]
    for line in f:
        if i%2==0:            
            text=""
            for char in line:
                if char not in bad_char:
                    text=text+char
            if text!="":
                binding_site.append(text)
        elif text!="":
            frequency=int(line)
            for num in range(frequency-1):
                binding_site.append(text)
        i+=1


with open("testing_set.txt","r") as f:
    bad_char=[" ","\n"]
    i=0
    testing_set=[]
    for line in f:
        if i%2==0:            
            text=""
            for char in line:
                if char not in bad_char:
                    text=text+char
            if text!="":
                testing_set.append(text)
        elif text!="":
            frequency=int(line)
            for num in range(frequency-1):
                testing_set.append(text)
        i+=1
    
with open("training_set.txt","r") as f:
    bad_char=[" ","\n"]
    i=0
    tree_learning_set=[]
    for line in f:
        if i%2==0:            
            text=""
            for char in line:
                if char not in bad_char:
                    text=text+char
            if text!="":
                tree_learning_set.append(text)
        elif text!="":
            frequency=int(line)
            for num in range(frequency-1):
                tree_learning_set.append(text)
        i+=1    

#print binding_site
#print len(binding_site)