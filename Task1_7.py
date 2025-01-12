year=int(input("enter a year:"))
if (year %4==0 and year %100!=0)or (year %400==0):
    leap_year= True
else:
    leap_year= False
print("is the year is a leap year?",leap_year)