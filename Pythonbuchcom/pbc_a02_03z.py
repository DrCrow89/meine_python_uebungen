# !/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    while True:
        try:
            n = int(input("Bitte Start eingeben: "))
            if n > 0:
                break
            else:
                print("Es muss eine Zahl größer 0 eingegeben werden!")
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

    zaehler = 0
    while n != 4:
        if (n%2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        zaehler += 1

    print(f"Nach {zaehler} Schritten endet die Folge in 4-2-1.")

if __name__ == '__main__':
    main()
