from datetime import date
todays_date=date.today()
print("curret date:" ,todays_date)
print("current year:",todays_date.year)
finalyear=int(input("enter the final year"))
for i in range(todays_date.year,finalyear):
    if (i % 400 == 0) or (i % 100== 0):
        print("{0} is a leap year".format(i))
    elif (i % 4 == 0) and (i%100!=0):
        print("{0} is a leap year".format(i))
    
    
