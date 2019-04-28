# !/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    for i in range(100, 1000, 1):
        hunderter = int(i/100)*100
        zehner = int((i - hunderter)/10)*10
        einer = i - hunderter - zehner

        hunderte_stelle = int(hunderter/100)
        zehner_stelle = int(zehner/10)

        ppdi = hunderte_stelle**3 + zehner_stelle**3 + einer**3

        if ppdi == i:
            print(i)

if __name__ == '__main__':
    main()
