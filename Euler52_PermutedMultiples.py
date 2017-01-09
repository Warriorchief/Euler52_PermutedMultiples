#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:26:56 2017

@author: christophergreen
Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly
 the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def is_permutation(x,y):
    if len(str(x))!=len(str(y)):
        return False
    chars=[];
    i=0;
    while i<len(str(x)):
        chars.append(str(x)[i]);
        i+=1;
    #print("from",x,"we have made the chars",chars);
    j=0;
    while j<len(str(y)):
        if str(y)[j] in chars:
            del chars[chars.index(str(y)[j])];  #find the first instance of the char in str(x) and deletes it
        else:
            return False;
        j+=1;
    #print("having removed matches one at a time, x still has the chars:",chars);
    if len(chars)==0:
        return True;
    else:
        return False;

def main(maximum):
    x=1;
    while x<=maximum:
        if is_permutation(x,2*x) and is_permutation(x,3*x) and is_permutation(x,4*x) and is_permutation(x,5*x) and is_permutation(x,6*x):
            print("found it! the number",x,"has the permutation multiples:",2*x,3*x,4*x,5*x,6*x);
            return x;
        x+=1;
    print("didn't find any number with these properties");
    return;

main(1000000) #found it! the number 142857 has the permutation multiples: 285714 428571 571428 714285 857142 CORRECT