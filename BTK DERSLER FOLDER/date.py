from datetime import datetime
from datetime import timedelta
simdi = datetime.now()
simdi = datetime.today()


result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%d')

t =  '27 October 1996 hour 09:30:31'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

birthday = datetime (1996,10,27,9,30,31)

result = datetime.timestamp(birthday) #saniye
result = datetime.fromtimestamp(result) #saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi- birthday # timedelta

result = simdi + timedelta(days= 10)


print(result)
