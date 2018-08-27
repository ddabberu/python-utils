

"""description: periodic scheduler along with basic timer function
   author: ddabberu"""

import os, time, datetime, threading

"""one time trigger"""
def wakeup_after_5seconds():
    t=threading.Timer(5.0,wokeup())
    t.daemon=True
    t.start()
def wokeup():
    global token
    token="blah"
token=''
#wokeup()
#print("printing token:{}".format(token))

"""periodic scheduler with time and apscheduler, background scheduler, interval triggers"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


"""define the func which will periodically invoke, we can have as many"""
def print_date_time():
    print("Current Time:{}".format(time.strftime("%A, %d. %B %Y %I:%M:%S %p")))
    return

def job2():
    print("Job2 starting at:{}".format(time.strftime("%A, %d. %B %Y %I:%M:%S %p")))
    return
###create and start scheduler
sched= BackgroundScheduler(daemon=True) #run this in bg
#add jobs
sched.add_job(print_date_time, 'interval', minutes=1) #interval scheduler like cron
sched.add_job(job2, 'interval', minutes=2) #interval scheduler like cron
sched.start()

#I am running a webserver to demonstrate the triggering of these jobs, periodically while server is serving clients---
#you may do anything else you like..
import http.server
import socketserver
handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",8080),handler) as httpd:
    print("Serving at port 8080")
    httpd.serve_forever()