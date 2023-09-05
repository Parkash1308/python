def showStudents(list):
    for i in list:
        print(i)

def removeStudent(student_list):
    print("list of student before removing student")
    showStudents(student_list)
    try:
        choice=int(input("Enter the index number to remove the student==>>> "))
        if choice >=0 and choice<len(student_list):
            removedStudent=student_list.pop(choice);
            print("List after removing the student")
            showStudents(student_list)
        else:
            print("Please Enter the valid index number")
    except ValueError:
        print("Enter the valid index number")


def addStudent(student_list):
    print("current list of student")
    showStudents(student_list)
    new_student=input("Enter the name of student ====>>>> ")
    student_list.append(new_student)
    print("Updated list of students" )
    showStudents(student_list)

def main():
    print("welcome to student portal")
    list=["Parkash", "hismat", "islam"]
    while True:
        print(" 1 To add a student ")
        print(" 2 To remove the student")
        print(" 3 To show the students list")
        print(" 4 To exit the application")
        choice=input("Enter the number to processed ahead ===>>>>  ")
        if(choice== "1"):
            addStudent(list)

        elif(choice== "2"):
            removeStudent(list)
        elif(choice== '3'):
            showStudents(list)
        else:
            break

if "__name__ =__main__" :
    main()