#Create the nested dictionary
students = {
    350: {"name": {"first_name": "Sagnik", "surname": "Pal"}, "age": 15, "class": "10th"},
    314: {"name": {"first_name": "Ankur", "surname": "Pal"}, "age": 14, "class": "9th"},
    313: {"name": {"first_name": "Soumya", "surname": "Chatterjee"}, "age": 16, "class": "11th"}
}

#Sort the dictionary by roll number (keys)
sorted_students = dict(sorted(students.items()))

#Display the sorted records
print("Student Records Sorted by Roll Number:")
for roll, details in sorted_students.items():
    print(f"Roll Number: {roll}")
    print(f"  Name: {details['name']['first_name']} {details['name']['surname']}")
    print(f"  Age: {details['age']}")
    print(f"  Class: {details['class']}")
    print()
