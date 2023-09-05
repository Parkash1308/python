

def add_task(to_do_list):
    new_task=input("Enter the name of task==>> ")
    to_do_list.append([new_task, False])
def show_task(to_do_list):
    for i, task in enumerate(to_do_list, start=1):
        status="Done" if task[1] else "Not Done"
        print(f"{i},{task[0]} - {status}")
def remove_task(to_do_list):

    show_task(to_do_list)
    try:
        index=int(input("Enter the the task number to be removed==>> "))

        if index>=0 and index<len(to_do_list):
            to_do_list.pop(index-1)
        else:
            print("Invalid input")

    except ValueError:
        print("Invalid input")

def mark_as_done(to_do_list):
    show_task()

    try:
        index=int(input("Enter the task number to mark as done==>> "))
        if index>=0 and index<len(to_do_list):
            to_do_list[index-1][1]=True
        else:
            print("Invalid input")

    except ValueError:
        print("Invalid input")

def main():
    print("Welcome To To Do App")
    list=[]

    while True:

        print(" 1 To Add Task")
        print(" 2 Display the To Do List")
        print(" 3 Mark task as done")
        print(" 4 remove task")
        print(" 5 exit")
        choice=input("Enter the choiceEnter the choice==>> ")

        if choice =="1":
            add_task(list)

        elif choice =="2":
            show_task(list)

        elif choice == "3":
            mark_as_done(list)
        elif choice=="4":
            remove_task(list)
        else:
            print("GOOD BYE")
            break

if "__name__ =__main__" :
    main()
