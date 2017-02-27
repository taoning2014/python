#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:01:33 2017

@author: Vivian
"""

annal_salary = float(input('Enter your starting annual salary:'))
min_portion_saved = 0
max_portion_saved = 10000
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
t = 0
count = 0
# bisection search range from (0,10000)
while t != 36:
    t = 0
    count = count + 1
    current_savings = 0
    temp_annal_salary = annal_salary
    while current_savings - total_cost * portion_down_payment < -100:
             current_savings = current_savings + temp_annal_salary / 12 * (min_portion_saved + max_portion_saved) / 10000 / 2 + current_savings * r / 12
             t = t + 1
             if t % 6 == 0:
                 temp_annal_salary = temp_annal_salary * (1 + semi_annual_raise)
    if t > 36:
        min_portion_saved = (min_portion_saved + max_portion_saved) / 2
    elif t < 36:
        max_portion_saved = (min_portion_saved + max_portion_saved) / 2
print ('Number of months: ',t) 
print ('Best savings rate:',(min_portion_saved + max_portion_saved) / 20000 )
print ('Steps in bisection search:', count)
