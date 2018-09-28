import robot
r = robot.rmap()
r.lm('task1')

def task():
    r.sleep=0.5
    r.rt()
    while not r.wr():
        while not r.wd():
            r.dn()
            r.up()
            r.rt()
        r.rt()

r.start(task)