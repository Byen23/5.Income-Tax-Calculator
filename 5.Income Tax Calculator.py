# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 06:05:55 2019

@author: Byen23
"""

# 5th Program 
'''Pseudocode: 
    1) Input the gross income and number of dependents 
    2) Compute the taxable income using the formula 
    3) Taxable income = gross income - 10000 - (3000 * number of dependents) 
    4) Compute the income tax using the formula 
    5) Tax = taxable income * 0.20 Print the tax'''
    
# Initalize the constants

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome- STANDARD_DEDUCTION - \
    DEPENDENT_DEDUCTION * numDependents

incomeTax = taxableIncome * TAX_RATE

# Display the income tax
print("The income tax is $" + str(incomeTax))





    
