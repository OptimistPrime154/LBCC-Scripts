import csv


name = input("What is your name? ")
home = input("Where do you live? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})