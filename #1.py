#create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
#your name is (blank), you are (blank) years old, and your username is (blank)
#for extra credit, have the program log this information in a file to be accessed later.


print("Please enter your name:")
name = input()
print("Thank you " + name + ". Could you please tell me how old are you?")
age = input()
print("Please tell me what is your reddit username?")
username = input()
print("your name is " + name + ", you are " + age + " years old, and your username is " + username)

file = open("log.txt", "w+")
file.write("Name: " + name + ", age: " + age + ", username:" + username)
file.close()

