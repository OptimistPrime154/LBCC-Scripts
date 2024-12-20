fname = input("What is your first name? ").strip().title()
lname = input("What is your last name? ").strip().title()
age = int(input("How old are you? "))

print (f"Your name is {fname} {lname} and you are {age} years old.")
print (f"{fname}, in ten years you will be {age + 10}!")

# Code academy code practice

credits = int(input("How many credits do you have? "))
gpa = float(input("What is your GPA? "))
if (credits >= 120) and (gpa >= 2.0):
  print("You have enough credits and units to graduate.")
else:
  print ("You do not meet one or both of the requirements to graduate.")
