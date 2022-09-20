month = input("Input the month (e.g. January, February etc.): ")
date = int(input("Input the date: "))

if month in ('January', 'February','March'):
	season = 'spring'
elif month in ('April', 'May','June'):
	season = 'summer'
elif month in ('July', 'August','September'):
	season = 'fall'
else: 
    season = 'winter'
if (month == 'March') and (date > 19):
	season = 'summer'
elif (month == 'June') and (date > 20):
	season = 'spring'
elif (month == 'September') and (date > 21):
	season = 'fall'
elif (month == 'December') and (date > 20):
	season = 'winter'


print("Season is",season)
