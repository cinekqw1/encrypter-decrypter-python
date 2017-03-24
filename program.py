#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from random import seed, randint
import os
import codecs
import sys



 
# funkcja kodujaca ciagi znakow
# x - string
# key - klucz 
def encrypt(x,key):
    result = ""
    seed(((954938*key)%0xFFFFFF)+2) #ziarno generatora liczb losowych
    for i in x:
      result+=   str(chr((ord(i)+int(randint(1, 10000))+3)%256)) #Funkcja kodujaca znak char
      
    return result
  
def decrypt(x,key):
    result = ""
    seed(((954938*key)%0xFFFFFF)+2) #ziarna generatora sa takie same
    for i in x:
      result+=  str(chr((ord(i)-int(randint(1, 10000))-3)%256)) #Funkcja dekodujaca znak char
      
    return result
 
 
def encrypt_file(x,y,k):

    if os.path.exists(x): # funkcja sprawdzajace sciezke do pliku
	plik = codecs.open(x, mode='r+',errors='ignore')
    else:
      print(CRED + "Error: Nie ma takiego pliku" + CEND)
      sys.exit()
	
    plik2 = codecs.open(y, mode='w+',errors='ignore')
    
    try:
	data = plik.read()
	plik2.write(encrypt(data,k))
	
    finally:
	plik.close()
	plik2.close()


def decrypt_file(x,y,k):

    if os.path.exists(x):
	plik = codecs.open(x, mode='r+',errors='ignore')
    else:
      print(CRED + "Error: Nie ma takiego pliku" + CEND)
      sys.exit()
      
    plik2 = open(y, 'w')
    
    try:
      
	data = plik.read()
	plik2.write(decrypt(data,k))
	
    finally:
      
	plik.close()
	plik2.close()
    
def RepresentsInt(s): # Funkcja sprawdzajaca czy jej argument da sie zamienic na typ integer
    try: 
        int(s)
        return True
    except ValueError:
        return False


#deklaracja kolorow 
CGREEDN = '\33[32m'
CRED = '\033[91m'
CEND = '\033[0m'








print "Uwagi:"
print "- Program stosuje szyfrowanie na bazie dwóch kluczy. "
print "- Pamiętaj aby klucze wysyłać różnymi środkami komunikacji.(e-mail, sms)"
print "- Kolejność wpisywania kluczy jest dowolna"
print "1.zakoduj plik"
print "2.odkoduj plik"

response = raw_input("Wybierz opcję (1 / 2): ")



if RepresentsInt(response):
    if int(response)==1 or int(response)==2:
	while(True):
	    file_1 = raw_input("Wpisz nazwe pliku: (input ) ")
	    if "." in file_1: 
		break
	    else:
		print(CRED + "Wpisz rozszerzenie" + CEND)
		
		
	while(True):	
	    file_2 = raw_input("Wpisz nazwe pliku docelowego: (output) ")
	    if "." in file_2: 
		break
	    else:
		print(CRED + "Wpisz rozszerzenie" + CEND)    
	 
	
	
	while(True)  :
	    key = raw_input("Wpisz klucz szyfrujacy/deszyfrujacy: ")
	
	    if RepresentsInt(key):
		break;
	    else:
		print(CRED + "Klucz musi byc typem integer" + CEND)
	while(True)  :
	    key2 = raw_input("Wpisz klucz szyfrujacy/deszyfrujacy 2: ")
	
	    if RepresentsInt(key):
		break;
	    else:
		print(CRED + "Klucz musi byc typem integer" + CEND)
	
	if int(response)==1:
	    encrypt_file(file_1,'temp_x.txt',int(key))
	    encrypt_file('temp_x.txt',file_2,int(key2))
	    os.remove('temp_x.txt')
	    print(CGREEDN + "Suceess" + CEND)
	if int(response)==2:
	    decrypt_file(file_1,'temp_x.txt',int(key))
	    decrypt_file('temp_x.txt',file_2,int(key2))
	    os.remove('temp_x.txt')
	    print(CGREEDN + "Suceess" + CEND)
    else:
	print(CRED + "Error: wpisz 1 lub 2" + CEND)

else:
  print(CRED + "Error: wpisz numer opcji ktora chcesz wybrac" + CEND)
  
  
  
  
  
  
  
  
  






 
