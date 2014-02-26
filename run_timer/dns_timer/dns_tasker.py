#coding:utf-8
#!/usr/bin python

import os
import sys
import time
from restful_lib import Connection
from daemon import Daemon
from celery import chain
from tasks import dnsprobe

import settings
import logging
import simplejson as json

class MyDaemon(Daemon):
    def run(self):
        main()

def init_log():
    if settings.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
            level=level,
            format='%(asctime)s [%(levelname)s] %(message)s',
            filename=settings.LOG_FILE,
            filemode='a+'
    )

def main():
    while True:
        try:
            client = Connection(settings.DATA_CENTER_ADDRESS)
            response = client.request_get('/dns_detection/interface/tasker')
            response = json.loads(response['body'])
            for k in response:
                dig = dnsprobe.subtask(args=((k),), exchange="detect",routing_key="dnsagent")
                res = chain(dig).apply_async()
                logging.info(str(res))
                client.request_get('/dns_detection/interface/tasker/'+str(k['id'])+'/status')
            time.sleep(1)

        except Exception, e:
            logging.error(str(e))
            

if __name__ == '__main__':
    init_log()

    try:
        my_daemon = MyDaemon('/var/run/dns_tasker.pid', home_dir='/tmp')
        if len(sys.argv) == 2:
            if 'start' == sys.argv[1]:
                my_daemon.start()
            elif 'stop' == sys.argv[1]:
                my_daemon.stop()
            elif 'restart' == sys.argv[1]:
                my_daemon.restart()
            elif '-d' == sys.argv[1]:
                main()
            else:
                print 'Unknown command'
                sys.exit(2)
            sys.exit(0)
        else:
            print 'Usage: %s start|stop|restart' % sys.argv[0]
            sys.exit(2)
    except Exception, e:
        logging.error(str(e))

