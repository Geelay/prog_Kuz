import robot
r = robot.rmap()
r.lm('task1')

def task():
    r.sleep=0.02
    while not r.wu():
        if r.label() == 'red':         
            r.pt()
        r.up()
    while not r.wd():        
        while not r.wl():
            if r.label() == 'red':         
                r.pt()
            r.lt()
        while not r.wr():
            if r.label() == 'red':         
                r.pt()
            r.rt()
        if r.wr():
            r.dn()
  
r.start(task)