# -*- coding: utf-8 -*-
"""Export tizimlari.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G1vNtWQYBFWgsT3dfo0EXnYjF_B_-6gb
"""

def tashxis(belgi):
   if belgi  == "istima":
      return "Parasetamol iching"
   elif belgi == "bosh og'riq":
      return"Trimol iching"
   elif belgi== "Tish og'riq":
      return  "Quepen iching"
   elif belgi== "Burun oqishi":
      return  "Loratadin"
   elif belgi == "Grip kasalligi":
      return"Antiviral preapatlar iching"
   elif belgi == "Asab tizimi kasalliklari":
      return"Sertalin iching"
   elif belgi == "Allergik kasalliklar":
      return"Loratadin iching"
   elif belgi == "Jigar kasalliklari":
      return"Furosemid"
   elif belgi == "Oshqozon og'riq":
      return"Noshpi iching"
   elif belgi == " Diabet og'riq":
      return"Metformin iching"
   elif belgi == " Qon tomirlar og'riq":
      return"Statinlar iching"
   else:
      return "Shifokorga murojat qiling"
belgi=input("Kasallik belgisini kiriting")
natija=tashxis(belgi)
print(natija)

def mashina(speed):
   if speed  == "120 km/h":
      return "Matiz"
   elif speed  == "250 km/h":
      return "BMW"
   elif speed  == "150 km/h":
      return "Mazeratti"
   elif speed  == "260 km/h":
      return "Dodge"
   elif speed  == "180 km/h":
      return "Chevrolet"
   elif speed  == "270 km/h":
      return "Mustang"
   elif speed  == "240 km/h":
      return "Captiva"
   elif speed  == "350 km/h":
      return "Jaguar"
   elif speed  == "190 km/h":
      return "Ford"
   elif speed  == "200 km/h":
      return "Kia"
   elif speed  == "980 km/h":
      return "Hyundai"
   else:
      return "bunday mashina mavjud emas"
speed=input("Mashina tezligini kiriting: ")
natija=mashina(speed)
print(natija)