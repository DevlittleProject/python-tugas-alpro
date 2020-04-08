import time
import calendar

ticks = time.time()

print "Berjalan sejak 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time()) 
print "Waktu lokal saat ini :", localtime

localtime = time.asctime( time.localtime(time.time()) )

print "Waktu lokal saat ini :", localtime

#CALENDAR
print("\n")
cal = calendar.month(2008, 1)

print "Dibawah ini adalah kalender:"

print cal