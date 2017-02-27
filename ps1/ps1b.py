#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 22:27:26 2017

@author: Vivian
"""

annal_salary = float(input('Enter your starting annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal:'))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
t = 0
while current_savings < total_cost * portion_down_payment:
    t = t + 1
    current_savings = current_savings + annal_salary / 12 * portion_saved + current_savings * r / 12
    if t % 6 == 0:
        annal_salary = annal_salary * (1 + semi_annual_raise)
print('Number of months: ',t)
