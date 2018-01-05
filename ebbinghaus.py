#!/usr/bin/env python
# -*- coding:utf-8 -*-

def printPlanOneDay( days, time, forget ):
    forgetTime = [2, 4, 7, 15]
    print("第", days + 1, "天", "     list", time + 1, end=' ')
    for forget in forgetTime:
        if ((time + 1) > forget - 1):
            print("     *list", ((time + 1) - (forget - 1)), end=' ')
    print("     *list", time + 1)

def getPlan( listNum ):

    print("			新学		背诵")
    forgetTime = [2, 4, 7, 15]
    days = 0
    forget = 0
    while days < listNum:
        printPlanOneDay(days,days, forget)
        days += 1
    lastTime = listNum + 15
    while lastTime >= 0:
        printPlanOneDay(days, lastTime, forget)
        lastTime -= 1
        days += 1




