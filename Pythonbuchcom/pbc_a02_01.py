# !/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    print("-----Sum that-----")
    summe = 0
    for i in range(0,10001,1):
        if ((i%7 == 0)and(i%5 != 0)):
            summe = summe + i
    print(f"Die Summe ist: {summe}")

if __name__ == '__main__':
    main()
