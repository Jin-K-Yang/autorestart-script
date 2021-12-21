import os
import sys
import time

def check_pid(pid):        
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

while True:
    pidfile = "./bot.pid"

    f = open(pidfile, 'r')
    pid = f.read().strip()
    if check_pid(int(pid)):
        print("bot already started")
    else:
        os.system("nohup yarn liquidator & echo $! > " + pidfile)
    time.sleep(60)