
import random
import string


first_name = input("Enter First Name:\n")
# first_name = str(first_name)
last_name = input("Enter last Name:\n")
# last_name = str(last_name)
email = input("Enter Email:\n")

# def random_password(length=5):
length = 5
random.choice(string.ascii_letters)
a = ''.join(random.choice(string.ascii_letters)for i in range(length))
print("This is your password:", a)


def password_check(new_password):
    if len(new_password) < 7:
        print("Password length should be at least 7")
        new_password = input("Enter new password:\n")


password = input("Enter 'Satisfied' if satisfied with password and 'Not satisfied' otherwise:\n")

# string and list slicing
hng = ['learn', 'coder', 'python']
name = ['First name:', first_name, 'Last name:', last_name, 'Email:', email]

if password == 'Satisfied':
    for item in name:
        print(item)

else:
    new_password = input("Enter new password:\n")

    if password_check(new_password):
        new_password = input("Enter new password:\n")
    else:
        for item in name:
            print(item)
