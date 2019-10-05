# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:49:31 2019

@author: tunggalmat
"""
#this code is to clear spyder console
from IPython import get_ipython

#make beautifull text in console
from pyfiglet import Figlet
f = Figlet(font='slant')

#import my lib quran
from Lib.QURAN import cari
cr = cari()

#code below is to clear cmd
#import os
#clear = lambda: os.system('cls')
#clear()#if use cmd console

loop = True
while loop :   
    get_ipython().magic('clear') #clear()#if use cmd console
    print(f.renderText('AL-QURAN'))
    print('1. Search by Surah & Ayah')
    print('2. Search by Surah')
    print('3. Search by Juz')
    print('4. Search by Word')
    print('5. EXIT')
    choice = input('---------------------\nYour Choice (1-5) : ')
    if choice == '1' :
        get_ipython().magic('clear') #clear()#if use cmd console
        print ('Search by Surah and Ayah\n')
        S,A = input('Surah(number) : '),input('Ayah(number) : ')
        z = cr.SurahAyah(int(S),int(A))
        get_ipython().magic('clear') #clear()#if use cmd console
        print('Surah  : ',S,' , Ayah : ',A)
        cr.show(z)        
        
    elif choice == '2' :
        get_ipython().magic('clear') #clear()#if use cmd console
        print ('Search by Surah\n')
        S = input('Surah(number) : ')
        z = cr.Surah(int(S))
        cr.show(z)
        
    elif choice == '3' :
        get_ipython().magic('clear') #clear()#if use cmd console
        print ('Search by Juz(number)\n')
        J = input('Juz : ')
        z = cr.Juz(int(J))
        cr.show(z)
        
    elif choice == '4' :
        get_ipython().magic('clear') #clear()#if use cmd console
        print ('Search by Word\n')
        W = input('Keyword : ')
        z = cr.Word(W)
        cr.show(z)
        
    elif choice == '5' : 
        get_ipython().magic('clear') #clear()#if use cmd console
        loop = False
        
    else :
        input('\nInvalid Input\nPress Enter to continue...')