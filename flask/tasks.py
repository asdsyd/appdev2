from celerytasks import celerytask

@celerytask.on_after_finalize.connect
def setup_periodic_task(sender,**kargs):
    sender.add_periodic_task(10.1,puchi.s(),name="print task")

@celerytask.task()
def puchi():
    print("puchi")

@celerytask.task()
def add(a,b):
    print(a+b)
    return a+b

