import re
import shelve
from datetime import date, datetime

"class that will manage my list"


class MyList:
    Agenda = shelve.open('database.dat', writeback=True)  # create a storage that are working as dictionary
    Date = re.compile("(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/([0-9]){4}")  # make a format for a date DD/MM/YYYY
    Time = re.compile("^([01]?[0-9]|1[012]):([0-5]?[0-9]) (AM|PM)")  # make a format for the time HH:MM AM

    def __init__(self, name):  # create a constructor that will take the name of the person who want to add a list
        self.name = name
        print('*' * 90)
        Header = "WElCOME *" + name + "* TO YOUR [TO DO APP]"
        print(str(Header).center(90))
        print('The application made up to manage your tasks!'.center(90))
        print('*' * 90)
        print()

    def getName(self):  # get the name of the person
        name = self.name
        return name

    def setTask(self, task):  # set the task that you want to add in your list
        choice = input("Do you want to (Save or Cancel): ")
        if choice.title() == "Save":
            print('Your task has been successful added\n')
            self.task = task
            return task
        elif choice.title() == "Cancel":
            return
        else:
            return

    def getTask(self):  # get the task
        task = self.task
        return task

    def setStatus(self, status):  # set the status
        if status.lower() == 'done' or status.lower() == 'not done':
            choice = input("Do you want to (Save or Cancel): ")
            if choice.title() == "Save":
                print('your Status has been saved\n')
                self.status = status
                return status
            elif choice.title() == 'Cancel':
                status = str(input('Enter the status of your task (Done or Not done): '))
                self.setStatus(status)
            else:
                self.setStatus(status)
        else:
            print('please! Enter the correct state! Example: done\n')
            status = str(input('Enter the status of your task (Done or Not done): '))
            self.setStatus(status)
            self.status = status

    def getStatus(self):  # get the status
        status = self.status
        return status

    def setDate(self, task_date):  # set the date
        if re.search(self.Date, task_date) is not None:  # check if the date respect the format(DD/MM/YYYY)
            choice = input('Do you want to (Save or Cancel): ')
            if choice.title() == 'Save':
                print('Your date has been saved\n')
                self.task_date = task_date
            elif choice.title() == 'Cancel':
                task_date = input("Enter the date that you will execute your task (Eg: DD/MM/YYYY): ")
                self.setDate(task_date)
            else:
                self.setDate(task_date)
        else:
            print('\nPlease Try Again!! example: 31/12/2018')
            task_date = input("Enter the date that you will execute your task (Eg: DD/MM/YYYY): ")
            self.setDate(task_date)

    def getDate(self):  # get the date
        task_date = self.task_date
        return task_date

    def setTime(self, time_task):  # set the time
        if re.search(self.Time, time_task) is not None:  # check if the time respect the format(HH:MM AM)
            choice = input('Do you want to (Save or Cancel): ')
            if choice.title() == 'Save':
                print('Your time has been saved\n')
                self.time_task = time_task
            elif choice.title() == 'Cancel':
                self.setTime(time_task)
            else:
                self.setTime(time_task)
        else:
            print('Please Try Again!! Example: 31/12/2018\n')
            time_task = input("Enter the time that you will execute your task (Eg: HH:MM PM): ")
            print('\n')
            self.setTime(time_task)

    def getTime(self):  # get the time
        Time = self.time_task
        return Time

    def getDday(self):  # get the number of day between the day that you will execute your task and the current date
        date_task = self.getDate()
        Date = datetime.strptime(date_task, '%d/%m/%Y').date()  # convert a string to a datetime
        today = date.today()  # get the current date
        time_between = str(today - Date)
        number_of_day = time_between.split(' ')
        return number_of_day[0]  # return the number of day

    def Store(self):
        details = {}  # declare a dictionary that will store all the details of each task
        global position  # keep track of the position of each task in the Agenda
        Dday = self.getDday()
        if 0 < int(Dday):  # check if the date is already past
            print('***The date that you have entered is already past***\n')
            Dday = 0
        name = self.getName()
        if self.Agenda:  # check if the storage is empty
            for key, value in sorted(self.Agenda.items()):
                if name == value['Name']:  # the user is already stored in the agenda
                    position = value['Position']  # store the current position of the task corresponding to his name
                else:
                    position = 0  # when it is a new user that want to add a task in the non empty storage
            position = int(position) + 1
        else:  # case when the storage is empty
            position = 1
        details['Position'] = str(position)
        details['Name'] = name
        details['Task'] = self.getTask()
        details['Status'] = self.getStatus()
        details['Date'] = self.getDate()
        details['Time'] = self.getTime()
        details['D-Day'] = Dday
        self.Agenda[str(position)] = details  # store the dictionary to our storage Agenda

    def update(self):
        if self.Agenda:
            number = str(input('From the list above enter the Number of the corresponding Tasks that you want to '
                               'modify: ')) 
            print('What do you want to update: ')
            print('1.Task')
            print('2.Status')
            print('3.Date')
            print('4.Time')
            option = int(input('select by typing(1, 2, 3 or 4)?: '))
            for key, value in self.Agenda.items():
                if self.name == value['Name'] and number == value['Position']:  # check if the name exist in the Agenda
                    if option == 1:  # case for the task
                        task = str(input("Enter the mew task to replace the old one: "))
                        value['Task'] = task
                        break

                    elif option == 2:  # case for the status
                        status = str(input('Enter the status of your task (Done or Not done): '))
                        self.setStatus(status)
                        self.getStatus()
                        value['Status'] = status
                        break

                    elif option == 3:  # case for the date
                        task_date = input("Enter the date that you will execute your task (Eg: DD/MM/YY): ")
                        self.setDate(task_date)
                        task_date = self.getDate()
                        Dday = self.getDday()
                        value['Date'] = task_date
                        value['D-Day'] = Dday
                        break

                    elif option == 4:  # case for the time
                        time_task = input("Enter the time that you will execute your task (Eg: HH:MM PM): ")
                        self.setTime(time_task)
                        time_task = self.getTime()
                        value['Time'] = time_task
                        break
                    else:
                        return
                else:
                    print("\nPlease verified if the corresponding number of Tasks that you have entered exist in your "
                          "list") 
                    print('***AND TRY AGAIN***\n')

        else:
            print('\n***You cannot update your list****')
            print('Your list is empty\n')


    def delete(self):
        if self.Agenda:
            number = str(input('From the list above enter the Number of your task: '))
            for key, value in self.Agenda.items():
                if self.name == value['Name'] and number == value['Position']:  # according to the position and the name
                    del self.Agenda[key]  # before delete a task
                    print('Your has been successful deleted!\n')
                    break

        else:
            print('Your list is empty\n')

    def display(self):  # show my list
        fmt = '{{:{}}}{{:>{}}}{{:>{}}}{{:>{}}}{{:>{}}}{{:>{}}}'.format(10, 30, 15, 15, 15, 10)
        print('=' * 95)
        print(fmt.format('Number', 'Tasks'.ljust(30), 'Status'.center(9), 'Date'.center(15), 'Time'.center(15),
                         'D-Day'.ljust(0)))
        print('-' * 95)
        try:
            for key, value in sorted(self.Agenda.items()):
                if self.name == value['Name']:
                    print(fmt.format(value['Position'],
                                     str(value['Task']).ljust(30),
                                     str(value['Status']).title(),
                                     str(value['Date']), str(value['Time']),
                                     str(value['D-Day'])))
        except:
            pass
