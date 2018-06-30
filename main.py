from MyList import *  # import all in Mylist
import sys

name = input("Your name: ")
if name.isidentifier():  #
    do = MyList(name)  # create an instance of class Mylist
else:
    print('your name cannot be saved!')
    print('Enter one word that will correspond to your name. Egg:ulrich')
    print('AND TRY AGAIN!!)
    sys.exit()
while True:
    print('1.Add a task with its details')
    print('2.Show your list')
    print('3.Update your list')
    print('4.Delete a task')
    print('5.Exit')
    option = str(input("Type your choice: "))
    if option == '1':
        task = str(input('Enter your task: '))
        if task:  # check if your task is not empty
            task = do.setTask(task)
            status = str(input('Enter the status of your task (Done or Not done): '))
            do.setStatus(status)
            Date = task_date = str(input("Enter the date that you will execute your task (Eg: DD/MM/YYYY): "))
            do.setDate(Date)
            time_task = str(input("Enter the time that you will execute your task (Eg: HH:MM PM): "))
            do.setTime(time_task)
            do.Store()
        else:
            print('***We cannot save this task!***')
            print('you have to enter a word or sentence before save your task\n')

    elif option == '2':
        do.display()
        

    elif option == '3':
        do.display()
        do.update()

    elif option == '4':
        do.display()
        do.delete()

    elif option == '5':
        sys.exit()

    else:
        print('\n***Enter the appropriate number***\n')
