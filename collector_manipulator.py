print("Welcome to the student Data Organizer!\n")

print("Select an option:\n","1. Add Student\n","2. Display All Students\n","3. update Student Information\n","4. Delete Student\n","5. Display ubject offered\n","6. Exit")

students={}

while True:
    choice=int(input("\n Enter your choice:"))
    if choice==1:
        print("\nEnter Student details:")
        s_id=int(input("Student Id:"))
        name=input("Name:")
        age=int(input("Age:"))
        grade=input("Grade:")
        dob=input("Date of Birth(YYYY-MM-DD):")
        sub=input("Subjects(comma-seprated):")

        
        students[s_id]={
            "name":name,
            "age":age,
            "grade":grade,
            "dob":dob,
            "subjects":sub
        }
        print("\n Student added Successfully!")


    elif choice==2:
        print("\n--- Display All Students---")
        if not students:
            print("No Student Record Found.")
        for s_id,info in students.items():
            print(f"Student ID:{s_id} | Name:{info["name"]} | Age:{info["age"]} | Grade:{info["grade"]} | Date of Birth:{info["dob"]} | Subjects:{info["subjects"]} ")


    elif choice==3:
        s_id=int(input("Enter Student ID to update:"))
        if s_id in  students:
            students[s_id]["grade"]=input("Enter new Grade:")
            print("Information updated.")
        else:
            print("Student Id not found.")            

    elif choice==4:
        s_id=int(input("Enter Student ID to delete: "))
        if students.pop(s_id,None):
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")

    elif choice==5:
        print("\nSubjects Offered: Maths,Physics,english,Chemistry,Computer")


    elif choice==6:
        print("Exiting...Goodbye!")
        break
    else:
        print("Invalid choice.Please try again.")


        

