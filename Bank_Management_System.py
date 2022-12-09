import csv

# function to sign up.
def does_username_exist(username, password1):
    filename = './credentials.csv'
    with open(filename, 'a+') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row)
    try:
        col1 = [name for name in data[0]]
        col2 = [password for password in data[1]]
        if username in col1 or password1 in col2:
            print("username or password already exist")
            return True
        return False
    except IndexError as I:
        print(I)
        return False


def signup():
    username = str(input("enter your username:"))
    password1 = input("enter your password:")
    password2 = input("renter your password:")
    if password1 == password1 and does_username_exist(username, password1) == False:
        filename = './credentials.csv'
        with open(filename, 'a+', newline="") as file:  # new line is to remove the space between each line
            writer = csv.writer(file)
            # writer.writerow(["Usernames", "Password"])
            writer.writerow([username, password1])
            print("registration is succesful!")
    else:
        print("please try again.")


# function to log in
def login():
    username = str(input("enter your username:"))
    password1 = input("enter your password:")
    filename = './credentials.csv'
    if does_username_exist(username, password1) == True:
        data = []
        with open(filename, 'r+') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        # print(data)
        names = [column[0] for column in data]
        passwords = [column[1] for column in data]

        if username in names:
            for k in range(0, len(names)):
                if names[k] == username and passwords[k] == password1:
                    print("log in successful!")
        else:
            print("username or password is incorrect. please try again")
    else:
        print("Your account was not found")


def previous_menu():
    return False


# customer function uses the previous menu above
def customer():
    print(f"welcome customer")
    menu = input("choose from the options below\n1. Login\n2. Signup\n3. Previous Menu\n4.exit\n:")
    if int(menu) == 1:
        print("use login function login()")
        login()
    elif int(menu) == 2:
        print("use signup function signup()")
        signup()
    elif int(menu) == 3:
        print("Use Previous menu, previous_menu()")
        # print(previous_menu)
        return previous_menu()
    elif int(menu) == 4:
        print("exiting")
        return True

    else:
        print("exiting..")


def admin():
    print(f"welcome customer")
    menu = input("choose from the options below\n1. Login\n2. Previous Menu\n3.exit\n:")
    if int(menu) == 1:
        print("use login function login()")
        login()
    elif int(menu) == 2:
        print("Use Previous menu, previous_menu()")
        # print(previous_menu)
        return previous_menu()
    elif int(menu) == 3:
        print("exiting")
        return True
    else:
        print("exiting..")


program_is_on = False
step2 = True
while not program_is_on:
    question_1 = {1: "customer", 2: "Admin", 3: "Exit"}
    user = ""
    identity = input("1. customer\n2. Admin\n3. Exit\nWho are you? Enter the number:")
    try:
        a = identity
        # print(a.title())
        if a.title() == "Exit":
            print("Exiting.....")
            program_is_on = True
        elif int(a) == 1:
            user = question_1[1]
            program_is_on = customer()
            # program_is_on = True
            # print(program_is_on)
        elif int(a) == 2:
          
            user = question_1[2]
            program_is_on = admin()
        else:
            print("invalid input. try again")

    except:
        print(f"Oops! Value error occured. Try again using the specified numbers")
        program_is_on = False
