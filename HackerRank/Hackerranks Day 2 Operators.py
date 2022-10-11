# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 01:18:09 2020

@author: uzumakinagato
"""


def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost*tip_percent)/100
    tax = (meal_cost*tax_percent)/100
    totalCost = meal_cost+tip+tax
    print(round(totalCost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)