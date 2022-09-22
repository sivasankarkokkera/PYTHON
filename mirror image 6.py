My_Number = int(input("Please provide the number to be mirror: "))
mirror_Number = 0
while(My_Number > 0):
 Reminder = My_Number %10
 mirror_Number = (mirror_Number *10) + Reminder
 My_Number = My_Number //10
print("mirror of the provided number is = %d" %mirror_Number)
