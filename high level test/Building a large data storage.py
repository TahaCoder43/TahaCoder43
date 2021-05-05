# Data Storages
Students = dict()
# Storage Helper Variables
nested_dictionerys_key_dictionery_accesor = ""
Student_Adder = ""
Student_Name_Adder = ""
Student_Age_Adder = ""
Student_class_Adder = ""
Student_gender_adder = ""
Number_of_addits = 0
# Navigation variables
Option_Changer_Helper_1 = 1
Option_Changer_Helper_2 = 2
Add_Option_Changer_Helper_1 = 1
Add_Option_Changer_Helper_2 = 2
Add_Option_Changer_Helper_3 = 3
Add_Option_Changer_Helper_4 = 4
If_Else_helper_1 = 1
If_Else_helper_2 = 2
Help_of_View_and_add = ""
Help_of_Adds_and_Addits = ""
Help_of_Exit_and_Addits_and_Adds = ""
Help_of_Exit_and_Addits = ""
# Other variables
Error_Message = "ERROR:You may have messed with options read the options in the bracket"
while Option_Changer_Helper_1 != Option_Changer_Helper_2:
    Help_of_View_and_add = input("1)Do you want to view or add(options:view,add):")
    If_Else_helper_1 = 1
    while If_Else_helper_1 != If_Else_helper_2 :
        if Help_of_View_and_add == "view":
            If_Else_helper_1 = 2
            Option_Changer_Helper_1 = 1
        elif Help_of_View_and_add == "add":
            If_Else_helper_1 = 2
            Option_Changer_Helper_1 = 2
        else:
            If_Else_helper_1 = 3
        while If_Else_helper_1 == 3:
            print(Error_Message + "\t\t\t1")
            If_Else_helper_1 = 2
#add
while Add_Option_Changer_Helper_1 != Add_Option_Changer_Helper_2:
    Help_of_Adds_and_Addits = input(
        "2)Do you want to add students or add information to students(Options:adds,addits)"
    )
    if Help_of_Adds_and_Addits == "adds":
        Add_Option_Changer_Helper_3 = 3
    elif Help_of_Adds_and_Addits == "addits":
        Add_Option_Changer_Helper_3 = 5
    else:
        Add_Option_Changer_Helper_1 = 3
    while Add_Option_Changer_Helper_1 == 3:
        print(Error_Message + "\t\t\t2")
        If_Else_helper_1 = 1
    # This is the adds
    while Add_Option_Changer_Helper_3 == 3:
        Student_Adder = input("What is the Number of the student in school")
        Students[Student_Adder] = {"Name": "", "Age": "", "Class": "","Gender":""}
        Add_Option_Changer_Helper_3 = 6
        while Add_Option_Changer_Helper_3 == 6:
            Help_of_Exit_and_Addits_and_Adds = input(
                "3)Do you want to enter information to student or add more students(Options:exit,back,adds,addits)"
            )
            if Help_of_Exit_and_Addits_and_Adds == "exit":
                Add_Option_Changer_Helper_3 = 4
                Add_Option_Changer_Helper_1 = 2
            elif Help_of_Exit_and_Addits_and_Adds == "back":
                Add_Option_Changer_Helper_3 = 2
            elif Help_of_Exit_and_Addits_and_Adds == "addits":
                Add_Option_Changer_Helper_3 = 5
            elif Help_of_Exit_and_Addits_and_Adds == "adds":
                Add_Option_Changer_Helper_3 = 3
            else:
                print(Error_Message + "\t\t\t3")
    print(Students)
    # This is Addits function
    while Add_Option_Changer_Helper_3 == 5:
        Number_of_addits = int(input("How many students do you want to add information to:"))
        for x in range(Number_of_addits):
            nested_dictionerys_key_dictionery_accesor = input("Which student num do you want add information to")
            Student_Name_Adder = input("What is the name:")
            Students[nested_dictionerys_key_dictionery_accesor]["Name"] = Student_Name_Adder
            Student_Age_Adder = input("What is " + Student_Name_Adder + "'s age")
            Students[nested_dictionerys_key_dictionery_accesor]["Age"] = Student_Age_Adder
            Student_class_Adder = input("What is " + Student_Name_Adder + ",s class")
            Students[nested_dictionerys_key_dictionery_accesor]["Class"] = Student_class_Adder
            Student_gender_adder = input("What is " + Student_Name_Adder + "'s gender")
            Students[nested_dictionerys_key_dictionery_accesor]["Gender"] = Student_gender_adder
            print(Students)
            Add_Option_Changer_Helper_3 = 8
        while Add_Option_Changer_Helper_3 == 8:
            Help_of_Exit_and_Addits = input("3)Do you want to exit:(Options:exit,addits,back)")
            if Help_of_Exit_and_Addits == "exit":
                Add_Option_Changer_Helper_3 = 4
                Add_Option_Changer_Helper_1 = 2
            elif Help_of_Exit_and_Addits == "addits":
                Add_Option_Changer_Helper_3 = 5
            elif Help_of_Exit_and_Addits == "back":
                Add_Option_Changer_Helper_3 = 2
            else:
                print(Error_Message + "\t\t\t4")
                Add_Option_Changer_Helper_3 = 8


