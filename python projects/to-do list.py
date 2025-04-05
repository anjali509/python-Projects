def todo():
    tasks=[]
    while True:
        print('''=======To-Do List=======
        1.Add task
        2.Show task
        3.Remove task
        4.Exit''')
        opt=int(input("Enter Your Choice :"))
        if opt==1:
            work=input("Enter the task to add : ")
            tasks.append(work)
            print("Task added successfully...")
        elif opt==2:
            for i,task in enumerate(tasks):
                print(i+1,".",task)
        elif opt==3:
            take=int(input("Enter task you want to remove : "))
            tasks.pop(take+1)
            print("Removed succesfully.....")
        elif opt==4:
            return
        else:
            print("Enter correct option")

todo()
