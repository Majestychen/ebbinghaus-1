#!/usr/bin/env python
# -*- coding:utf-8 -*-

def getPlan( listNum ):
    forgetTime = {2, 4, 7, 15}

    print("			新学		背诵")
    forgetTime = [2, 4, 7, 15]
    days = 0
    forget = 0
    while days < listNum:
        print("第", days + 1, "天", "     list", days + 1, end=' ')
        days += 1
        for forget in forgetTime:
            if ((days + 1) > forget - 1):
                print("     *list", ((days + 1) - (forget - 1)), end=' ')
        print("     *list", days + 1)




