'''a school decided to replace the desks in 3 classrooms. each desk sits 2 students.given the number of students in each class.print the smallest possible number of desks that can be purchased
the program should read three integers : the number of students in each of the three classes a,b and c
'''
no_student_class1=int(input("enter the number of students in first class :"))
no_students_class2=int(input("enter the number of students in second class :"))
no_students_class3=int(input("enter the number of students in third class :"))

desk_class1=(no_students_class1//2)
print(f"the number of desk needed for class 1 is {desk_class1} ")
desk_class2=(no_students_class2//2)
print(f"the number of desk needed for class 2 is {desk_class2}")
desk_class3=(no_students_class3//2)
print(f"the number of desk needed for class 3 is {desk_class3}")

