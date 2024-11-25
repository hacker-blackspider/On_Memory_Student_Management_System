#Initializing Dictationary
student = {

}

#Adding a element
def add_student(name,grade):
    student[name]=grade
    print("Added {name} with a {grade}")

#updating 
def update_student(name,grade):
    if name in student:
        student[name]=grade
        print("{name} with marks are updated {grade}")
    else:
        print("{name} is not found!")
#delet
def del_student(name,grade):
    if name in student:
        del student[name]
        print("{name} are successfully Deleted ")
    else:
        print("{name} is not found!")
# show all Student Data
def show_All_student():
    if student:
        for name,grade in student.items():
            print(f"{name}:{grade}")
    else:
        print("No Student Found ")

def main():
    while(True):
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        Choice = int(input("Enter Your Choice :-- "))
        if Choice == 1:
            name=input("Enter Student Name : ")
            grade=int(input("Enter Student Grade : "))
            add_student(name,grade)
        elif Choice==2:
             name=input("Enter Student Name : ")
             grade=int(input("Enter Student Grade : "))
             update_student(name,grade)
        elif Choice==3:
            name=input("Enter Student Name : ")
            del_student(name)
        elif Choice==4:
            
            show_All_student()
            
        elif Choice==5:
            print("---------Closing The Student Management System---------")
            break
        else:
            print("------Invalid Credintials ------")

#__name__== "__main__"
main()
