student_data={"Rupak":{"Marks":85},"Sohan":{"Marks":90},"Riya":{"Marks":95}}
print("Enter Student Name :")
student_name=input()
if student_name in student_data:
    print("Marks of", student_name, "is", student_data[student_name]["Marks"])
else:
    print("Student not found")