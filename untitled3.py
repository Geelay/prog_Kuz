import robot
r = robot.rmap()
r.lm('task1')

def task():
    r.sleep=0.02
    while not r.wd():
        while not r.wr():
            r.pt()
            r.rt()
            r.dn()
            r.pt()
            r.up()
            r.rt()
            r.pt()
            r.rt()
            if not r.wr():
                r.rt()
        if r.wr():
            r.dn()
            r.dn()
            r.dn()
        while not r.wl():
            r.pt()
            r.lt()
            r.dn()
            r.pt()
            r.up()
            r.lt()
            r.pt()
            r.lt()
            if not r.wl():
                r.lt()

r.start(task)
