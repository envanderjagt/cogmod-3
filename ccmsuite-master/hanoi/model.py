import ccm
from ccm.lib.actr import *

class ModelHanoi(ACTR):
    goal = Buffer()
    subGoal1 = Buffer()
    subGoal2 = Buffer()
    
    def set_subGoal1(goal="current:A123BC target:!A123BC", subGoal1 = None):
        subGoal1.set('A1C1') #the biggest disk needs to go to the rigth peg

    #to simulate the first move wrong, as most people do, we do now this step:
    def move_disk3wrong(goal="current:A123BC target:!A123BC" subGoal1='A1C1'):
        goal.modify(current="A12B3C")
        print("Disk 3 was moved to peg B")
        print("Peg A has disks[1,2], peg B has disks [3], peg C has disks []")
        
    def set_subGoal2(goal="current:!A1B2C3", subGoal1="A1C1", subGoal2 = None):
        subGoal2.set("A2B2") #Disk 2 is in the way of disk 1 so we need to put it on a different peg where it will not be in the way anymore
        
    def move_disk1(goal="current:A123BC target:!A123BC", subGoal2 = 'A2B2'):
        goal.modify(current='A12BC3')# to accomplish subGoal2, we need to move disk 3 to peg C, else we cannot move disk 2 to peg B
        print("Disk 3 was moved to peg C")
        print("Peg A has disks[1,2], peg B has disks [], peg C has disks [3]")
        goal.modify(current='A1B2C3')# to accomplish subGoal1, we need to move disk 2 to peg B
        print("Disk 2 was moved to peg B")
        print("Peg A has disks[1], peg B has disks [2], peg C has disks [3]")
        subGoal2.clear()
        
    def move_disk2(goal="current:A1B2C3 target:!A1B2C3", subGoal1 = "A1C1"):
        goal.modify(current='A1B23C')# to accomplish subGoal1, we need to move disk 3 to peg B, else we cannot move disk 1 to peg C
        print("Disk 3 was moved to peg B")
        print("Peg A has disks[1], peg B has disks [2,3], peg C has disks []")
        goal.modify(current='AB23C1')# to accomplish subGoal1, we need to move disk 1 to peg C
        print("Disk 1 was moved to peg C")
        print("Peg A has disks[], peg B has disks [2,3], peg C has disks [1]")
        subGoal1.clear()
        
    def set_subGoal3(goal="current:AB23C1 target:!AB23C1", subGoal1 = None):
        subGoal1.set("B2C2") #the biggest disk, which is not yet on the rigth peg, needs to go to the rigth peg
        
    def move_disk3(goal = "current:AB23C1 target:!AB23C1", subGoal1 = "B2C2"):
        goal.modify(current='A3B2C1')# to accomplish subGoal1, we need to move disk 3 to peg A, else we cannot move disk 2 to peg C
        print("Disk 3 was moved to peg !")
        print("Peg A has disks[3], peg B has disks [2], peg C has disks [1]")
        goal.modify(current='A3BC12')# to accomplish subGoal1, we need to move disk 2 to peg C
        print("Disk 2 was moved to peg C")
        print("Peg A has disks[3], peg B has disks [], peg C has disks [1,2]")
        subGoal1.clear()
        goal.modify(current='ABC123')# to accomplish the goal, we need to move disk 1 to peg C
        print("Disk 3 was moved to peg C")
        print("Peg A has disks[], peg B has disks [], peg C has disks [1,2,3]")
        
        
model = ModelHanoi()
model.goal.set("current:A123BC target:ABC123")
model.run()