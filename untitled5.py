import robot
r = robot.rmap()
r.lm('task1')
y=0
slyapa=int(input())
nojka=int(input())
tt=slyapa//2
def task():
    r.sleep=0.02
    for y in range(0,slyapa)  :  
        r.pt()
        r.rt()
        
    


r.start(task)


