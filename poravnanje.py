# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 00:05:30 2020

@author: Ana
"""

def poklapanje(s1, s2): 
    a=len(s1) 
    b=len(s2) 
    br_d=0 
    br_l=0 
    maxx=0 
    min_br=0 
    # desna rotacija
    for i in range(a): 
        max_d=0 
        # proverava koji je string duzi da bi znali do kog clana stringa proveravamo poklapanje
        if(a<=b): 
            for j in range(a):
                if(s1[j]==s2[j]):
                    max_d+=1
            # cuvamo najveci
            if(max_d==maxx)and(br_d<min_br):
                maxx=max_d
                min_br=br_d
            if(max_d>maxx):
                maxx=max_d
                min_br=br_d
            # rotacija u desno            
            s1=s1[-1]+s1[:-1]
            br_d+=1
        else:
            for j in range(b):
                if(s1[j]==s2[j]):
                    max_d+=1
            if(max_d==maxx)and(br_d<min_br):
                maxx=max_d
                min_br=br_d
            if(max_d>maxx):
                maxx=max_d
                min_br=br_d
            s1=s1[-1]+s1[:-1]            
            br_d+=1
        
    # leva rotacija
    for i in range(a):
        max_l=0
        # proverava koji je string duzi da bi znali do kog clana stringa proveravamo poklapanje
        if(a<=b):
            for j in range(a):
                if(s1[j]==s2[j]):
                    max_l+=1
            # cuvamo najveci
            if(max_l==maxx)and(br_l<min_br):
                maxx=max_l
                min_br=br_l
            if(max_l>maxx):
                maxx=max_l
                min_br=br_l
            # rotacija u levo
            s1=s1[1:]+s1[0]
            br_l+=1
        else:
            for j in range(b):
                if(s1[j]==s2[j]):
                    max_l+=1
            if(max_l==maxx)and(br_l<min_br):
                maxx=max_l
                min_br=br_l
            if(max_l>maxx):
                maxx=max_l
                min_br=br_l
            s1=s1[1:]+s1[0]
            br_l+=1
            
    return (maxx, min_br)

    
s1 = "CTTCGAAAGCCATT"
s2 = "AACCTAGGCCA" 


poklapanje(s1, s2)

print(s1)
print(s2)

print(poklapanje(s1,s2))