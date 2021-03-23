#write a python program to convert seconds to day ,hour ,minutes and seconds
#changes
a=int(input("enter how much second would you like to convert to day ,hour ,minutes and seconds :"))
day=a/(60*60*24)
hour=a/(60*60)
minutes=a/60
print(f"Your converted hour time is :{hour}")
print(f"Your converted day time is :{day}")
print(f"Your converted minute time is:{minutes}")
print(f"Your given second is:{a}")


