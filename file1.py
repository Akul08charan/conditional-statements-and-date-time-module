city =(input("City name:"))
temp =float(input("Tempurature:"))

if temp>35:
    print("WARNING HOT!!!")

if temp >25:
    print("GREAT day to go OUTSIDE!!")
else:
    print("Grab a JACKET before you go OUT!")

if temp>35:
    print("REALLY HOT OUTSIDE!!!!")
elif temp>25:
    print("WARM and SUNNY!!!")
elif temp>15:
    print("COOL and BREEZY!!")
else:
    print("COLD!")

import datetime, calendar
x =datetime.datetime.now()
print(city,x)
y =calendar.calendar(x.year)
print(y)

 