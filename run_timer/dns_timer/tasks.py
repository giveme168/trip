from celery.task import task

@task(name="tasks.dnsprobe")
def dnsprobe(arg):
	print "post dns"

