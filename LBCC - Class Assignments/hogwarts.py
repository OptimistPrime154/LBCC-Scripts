students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
#code prints out all three names in seperate lines
    
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)): #for creates an interger. i is now an interger within the list
    print(i + 1, students[i])
#this code prints out the names with their index number left of their name by removing the 1.
    #the i + 1 changes to a formal list that ranges from 1 to 3

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
# this code printed the values which where Gryf*3 and Slyth once each in a new line

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",}

for student in students:
    print(student, students[student], sep=", ")
#code prints out name and house of student in a new line
    
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

