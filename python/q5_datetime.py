# Hint:  use Google to find python function
import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

a = datetime.datetime.strptime(date_start,"%m-%d-%Y")
b = datetime.datetime.strptime(date_stop,"%m-%d-%Y")

print(a.date())
print(b.date())

diff = b.date() - a.date()
print(diff)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

a = datetime.datetime.strptime(date_start,"%m%d%Y")
b = datetime.datetime.strptime(date_stop,"%m%d%Y")

print(a.date())
print(b.date())

diff = b.date() - a.date()
print(diff)



####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  


a = datetime.datetime.strptime(date_start,"%d-%b-%Y")
b = datetime.datetime.strptime(date_stop,"%d-%b-%Y")

print(a.date())
print(b.date())

diff = b.date() - a.date()
print(diff) 

