#-*- coding: utf-8 -*-


secret = 15

guess = int(raw_input("Vnesi skrito število:"))

if secret == guess:
    print("Bravo uganil si skrito število!")

else:
    print("Vneseno število ni pravo!")