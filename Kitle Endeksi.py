# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 23:00:54 2024

@author: lenovo
"""


        
#kullanıcının vücut kitle indexini hesaplayıp kullanıcıya verilen bilgiler ile yorumlamasını sağlayan program.

# Kullanıcıdan boy ve kilo bilgisini al
boy = float(input("Lütfen Boyunuzu Metre cinsinden Giriniz (Örneğin, 1.75): "))
kilo = float(input("Lütfen Kilonuzu Kilogram cinsinden Giriniz: "))

# VKİ hesapla
vki = kilo / (boy ** 2)

# VKİ'ye göre yorum yap
print("Vücut Kitle İndeksi (VKİ) =", vki)

if vki < 18.5:
    print("VKİ'niz: Zayıf")
elif 18.5 <= vki < 24.9:
    print("VKİ'niz: Normal")
elif 24.9 <= vki < 29.9:
    print("VKİ'niz: Fazla Kilolu")
elif 29.9 <= vki < 34.9:
    print("VKİ'niz: Şişman (Obez) - I. Sınıf")
elif 34.9 <= vki < 39.9:
    print("VKİ'niz: Şişman (Obez) - II. Sınıf")
else:
    print("VKİ'niz: Aşırı Şişman (Aşırı Obez) - III. Sınıf")

    
    
    

        

    
    
    

    