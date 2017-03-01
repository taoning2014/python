#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:27:25 2017

@author: Vivian
"""
annal_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home:'))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
number_of_month = 0
target = total_cost * portion_down_payment
monthly_savings = annal_salary / 12 * portion_saved
monthly_interest_rate = r / 12
while current_savings < target:
    number_of_month = number_of_month + 1
    pre_savings = current_savings
    current_savings = pre_savings + monthly_savings + pre_savings * monthly_interest_rate
print('Number of months: ',number_of_month)
