from tkinter import *

from tkinter.ttk import *
from typing import Any
from queue import PriorityQueue

class Task:

    def __init__(self,taskName,taskPriority,taskTime):
        #taskName = self.acceptTask()
        self.taskName = taskName
        self.taskPriority = taskPriority
        self.taskTime = taskTime
        #self.printName(taskName)


    def acceptTask (self):
        taskName = input("Aight gimme a description ofthat task that you don't wanna do: ")
        return taskName

    
    def printName (self):
        print(self.taskName)
    
    def getName(self):
        return self.taskName



class TaskKeeper:
    #array = []
    def __init__(self,array,taskQueue):
        #self.array = array
        self.makeArray(array,taskQueue)
        self.printArray(array,taskQueue)

    def printArray(self,array,taskQueue):
        print("Arrays: ")
        for task in array:
            print(task.getName())
        print("Priority Queue: ")
        while not taskQueue.empty():
            item = taskQueue.get()
            print(item)
             



    def makeArray(self,array,taskQueue):
        ifDo = 1
        while ifDo == 1:
            
            task1 = Task(self.acceptTaskName(),self.acceptTaskPriority(),self.acceptTaskTime())
            taskQueue.put((task1.taskPriority,task1.taskName))
            array.append(task1)
            print(task1.taskName)
            ifDo = int(input("Okay, do you have some tasks for me? (0 or 1): "))
        print("You entered something that wasn't 1, so I assume you're done. Bye nigger")
        return array


    def acceptTaskName(self):
        taskName = input("Aight gimme a description: ")
        while type(taskName) != str:
            taskName = input("Bro, a string.. cmon: ")
        return taskName
    
    def acceptTaskPriority(self):
        taskPriority = int(input("Priority, 0-2, 0 highest 2 lowest: "))
        while type(taskPriority) != int and (taskPriority != 1 or taskPriority != 2 or taskPriority !=0):
            taskPriority = input("Bro, I said an int, 0-2, dumbo: ")
        return taskPriority
    
    def acceptTaskTime(self):
        taskTime = float(input("Aight how long you think it's finna take (in hours): "))
        while type(taskTime) != float:
            taskTime = input("Bro, a number, a float, if you will: ")
        return taskTime


class GUI:
    popup = Tk()
    namevar = StringVar()
    descvar = StringVar()
    priority = StringVar()
    difficulty = StringVar()
    interest = StringVar()
    #frame = Frame(popup)

    taskCount = 0

    taskFrame = Frame(popup,height = 335,width = 625, style = 'taskFrame.TFrame')
    listbox = Listbox(taskFrame,height = 335, width = 625, fg= 'red')
    toolFrame = Frame(popup,height= 335, width = 150, style='toolFrame.TFrame')
    
    s = Style()
    
    def __init__(self):
        print("using tkinter")
        #self.frame.pack()
        self.popup.geometry('800x600')
        self.popup.title('Uhh I am testing')
        self.setUpButtons()
        self.setUpLabels()
        self.taskDisplay()
        self.popup.mainloop()


    def setUpButtons(self):
        button = Button(self.popup,text='Stop',width=25,
                                                command=self.popup.destroy)
        button.place(x=10,y=565)
        submitBtn = Button (self.popup,text = 'Enter', 
                        command = self.acceptInputs)
        submitBtn.place(x = 712, y = 565)

        self.toolFrame.place(x = 640, y = 20)
        self.s.configure('toolFrame.TFrame', background ='grey')
        clearBtn = Button(self.toolFrame,text="Clear", command=self.clearList)
        clearBtn.pack(anchor= 'center',side = TOP)
        fakeBtn1 = Button(self.toolFrame,text="Nothing",command=None)
        fakeBtn1.pack(anchor='center',side = TOP )

        removeBtn = Button(self.toolFrame,text="Remove Task", 
                                                command=self.removeTask)
        removeBtn.pack(anchor='center',side = TOP)

        
        
    def setUpLabels(self):
        label1 = Label(self.popup,text="Task List, or Queue.. whatever dude")
        label1.place(x = 317, y = 10, anchor= 'center')

        label2 = Label(self.popup, text="Tools")
        label2.place(x = 717, y = 10, anchor='center')

        taskName = Label(self.popup, text='Task')
        taskName.place(x = 10,y = 470)
        taskDesc = Label(self.popup, text='Description')
        taskDesc.place(x = 10,y = 500)
        

        nameIn = Entry(self.popup,textvariable= self.namevar, width= 40)
        nameIn.place(x = 43, y = 470)
        descIn = Entry(self.popup,textvariable= self.descvar, width= 60)
        descIn.place(x = 80, y = 500)

        priorityDrop = Label(self.popup, text='Priority')
        priorityDrop.place(x = 520, y = 470)

        #combobox - dropdown
        
        priorLvl = Combobox(self.popup,width=7,textvariable=self.priority)

        priorLvl['values'] = ('0 - High','1 - Mid','2 - Low','3 - Eh')
        priorLvl.place(x = 570, y = 470)

        diffDrop = Label(self.popup,text='Difficulty')
        diffDrop.place(x = 665,y=470)

        
        diffLvl = Combobox(self.popup,width=7,textvariable=self.difficulty)

        diffLvl['values'] = ('Hard','Eh','Easy')
        diffLvl.place(x= 722,y = 470)

        interestDrop = Label(self.popup,text='Interest Level')
        interestDrop.place(x = 315, y = 470)
        

        interestLvl = Combobox(self.popup,width=15,textvariable=self.interest)
        
        interestLvl['values'] = ('Cannot wait','Interested','Eh','Pls no','Oh dear God no')
        interestLvl.place(x = 395, y = 470)
    
    def taskDisplay(self):
        
        self.s.configure('taskFrame.TFrame',background = 'white')
        self.taskFrame.place(x = 10, y = 20)
        
        self.listbox.place( x = 0, y = 0)
        
    def addToDisplay (self,taskCount,name):
        
        
        self.listbox.insert(taskCount, name)

    def removeTask (self):
        #selected = self.listbox.curselection()
        self.listbox.delete(self.listbox.curselection())

    def clearList (self):
        self.listbox.delete(0,self.listbox.size())
        


        

    def acceptInputs(self):

        name = self.namevar.get()
        desc = self.descvar.get()
        prior = self.priority.get()
        if prior == "0 - High":
            prior = 0
        elif prior == "1 - Mid":
            prior = 1
        elif prior == "2 - Low":
            prior = 2
        elif prior == "3 - Eh":
            prior = 3
        #for now, if the priority is not one of the 4 then it's assigned lowest
        else:
            prior = 3
        diff = self.difficulty.get()
        if diff == "Hard":
            diff = 3
        elif diff == "Eh":
            diff = 2
        elif diff == "Easy":
            diff = 1
        else:
            diff = 1
        inter = self.interest.get()
        if inter == "Cannot wait":
            inter = 5
        elif inter == "Interested":
            inter = 4
        elif inter == "Eh":
            inter = 3
        elif inter == "Pls no":
            inter = 2
        elif inter == "Oh dear God no":
            inter = 1

        print("task name: "+name)
        print("description: "+desc)
        print("priority: "+str(prior))
        print("difficulty: "+str(diff)) 
        print("interest level: "+str(inter))

        self.taskCount += 1

        self.addToDisplay(self.taskCount,name)

        self.namevar.set("")
        self.descvar.set("")
        self.priority.set("")
        self.difficulty.set("")
        self.interest.set("")



        



        
        



        

    

#task1 = Task("do poop","0","2")
#print(task1.taskName)

###### TASK STUFF ###########
#taskArray = []

#taskQueue = PriorityQueue()


#taskthing = TaskKeeper(taskArray,taskQueue)

######### GUI ########
gui = GUI()

