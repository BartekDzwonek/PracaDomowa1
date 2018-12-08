#!/usr/bin/env python3


class Kwiatek:
    def __init__(self, kolor, nazwa):
        self.kolor = kolor
        self.nazwa = nazwa

    def wyswietl(self):
        print("Kolor kwiatka to {} a jego nazwa to {}".format(self.kolor, self.nazwa))


kolor = input("Podaj kolor kwiatka: ")
nazwa = input("Jak nazywa sie kwiatek: ")

kwiatek = Kwiatek(kolor, nazwa)
kwiatek.wyswietl()
