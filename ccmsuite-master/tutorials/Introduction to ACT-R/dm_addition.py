import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

class Addition(ACTR):
  goal=Buffer()
  retrieve=Buffer()
  memory=Memory(retrieve,threshold=-3)
  DMNoise(memory,noise=0.3)
  
  def init():
    for i in range(100):
      string = 'count %s %s' % (str(i),str(i+1))
      memory.add(string)
  
  def initializeAddition(goal='add ?num1 ?num2 count:None?count sum:None?sum'):
    goal.modify(count=0,sum=num1)
    memory.request('count ?num1 ?next')
    
  def terminateAddition(goal='add ?num1 ?num2 count:?num2 sum:?sum'):
    goal.set('result ?sum')
    print sum
    
  def incrementSum(goal='add ?num1 ?num2 count:?count!?num2 sum:?sum',
                   retrieve='count ?sum ?next'):
    goal.modify(sum=next)
    memory.request('count ?count ?n2')
    
  def incrementCount(goal='add ?num1 ?num2 count:?count sum:?sum',
                     retrieve='count ?count ?next'):
    goal.modify(count=next)
    memory.request('count ?sum ?n2')

model=Addition()
ccm.log_everything(model)
x = str(input("first: "))
y = str(input("second: "))
string = 'add %s %s count:None sum:None' % (str(x),str(y))
model.goal.set(string)
model.run()

