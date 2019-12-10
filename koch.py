# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:20:22 2019

@author: Eve
"""

import turtle
bob = turtle

def koch(t, length):
    
    for i in [60, -120, 60, 0]:
            t.fd(length/3)
            t.lt(i)
    

def koch_curve(t, length, n):
    
    if n == 0:
        t.fd(length)
        return
    m = length/3
    
    for i in [60, -120, 60, 0]:
            koch_curve(t, m, n-1)
            t.lt(i)
            
            
def koch_snowflake(t, length, stage):
    
    t.delay(-400)
    for i in range (3):
        for i in [-120, 60, -120, 60]:
            koch_curve(t, length, stage)
            t.lt(i)
        
    
koch_snowflake(bob, 100, 5)