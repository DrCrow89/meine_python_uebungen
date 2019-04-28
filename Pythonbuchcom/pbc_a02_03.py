# !/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    while True:
        try:
            a = int(input("Bitte Start eingeben: "))
            b = int(input("Bitte Ende eingeben: "))
            if a < b:
                break
            else:
                print("Ende muss größer als Start sein!")
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

    for i in range(a,b+1,1):
        n = i
        zaehler = 0
        while n != 0:
            if (n%3 == 0):
                n = n + 4
            elif ((n%3 != 0) and (n%4 == 0)):
                n = n/2
            elif ((n%3 != 0) and (n%4 != 0)):
                n = n - 1
            else:
                print(f"Fehler bei n = {i}")
                break
            zaehler += 1
        print(f"{i} -> {zaehler}")

if __name__ == '__main__':
    main()
