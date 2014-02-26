from kombu import Exchange, Queue

BROKER_URL = "amqp://guest:guest@127.0.0.1:5672//" 
CELERY_RESULT_BACKEND = "amqp" 
CELERY_IMPORTS = ("tasks", )

#CELERY_QUEUES = (
    #Queue('node1', Exchange('detect'), routing_key='node1'),
#)

#CELERY_ROUTES = {
    #'tasks.tcp_ping':  {'queue': 'node1'},
    #'tasks.icmp_ping': {'queue': 'node1'},
#}
