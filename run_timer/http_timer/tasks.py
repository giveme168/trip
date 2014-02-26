from celery.task import task

@task(name="tasks.dnsprobe")
def dnsprobe(arg):
	print "post dns"

@task(name="tasks.tcp_ping")
def tcp_ping(arg):
	print "post dns"