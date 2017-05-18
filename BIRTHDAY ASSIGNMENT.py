
import calendar  #importing inbuilt calendar module
M=input("Which year were you born?\n")
N=input("Enter your month of birth number among the 12  months \n")        
L=input("Enter the date(1-31)\n")
DAY=calendar.weekday(year=int(M), month=int(N), day=int(L)) 



#Applying a conditional func

    #Applying a conditional function to assign the result from the module used to the respective day
if DAY == 0:
    y = "Monday"
elif DAY == 1:
    y = "Tuesday"
elif DAY == 2:
    y = "Wednesday"
elif DAY == 3:
    y = "Thursday"
elif DAY == 4:
    y = "Friday"
elif DAY == 5:
    y= "Saturday"
else:
    y = "Sunday"

print("We you were born on "+y)
input("Press enter")
