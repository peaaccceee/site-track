name = input("What's the name of your construction project? ")
location = input("Where is the construction project located? ")
duration = input("What is the expected duration of the project? ")

print('Project Name: ' + name)
print('Location: ' + location)
print('Expected Duration: ' + duration + "weeks")

progress = int (input("What is the current progress of the project?"))
if progress == 100:
    print("The project is complete!")
elif progress > 0:
    print("The project is in progress.")
else:
    print("Not started.")
