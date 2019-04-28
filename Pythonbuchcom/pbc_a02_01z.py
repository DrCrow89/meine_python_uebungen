# !/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    print("-----Sum that-----")
    ergebnis_liste = [i for i in range(0,10001,1) if ((i%7 == 0)and(i%5 != 0))]
    print(f"Die Summe ist: {sum(ergebnis_liste)}")

if __name__ == '__main__':
    main()
