from functions import *

cart = {}
fast_food_menu = {
    "burger": {"price": 250},
    "fries": {"price": 50},
    "pizza": {"price": 450},
    "chicken_wings": {"price": 400},
    "hot_dog": {"price": 300},
    "taco": {"price": 150},
    "sandwich": {"price": 200},
    "salad": {"price": 70},
    "ice_cream": {"price": 50},
    "soda": {"price": 60},
}
print("Welcome To QuickBite Express\n1. LOGIN\n2. SIGNUP\n3. EXIT")
users = []

while True:
    try:
        with open("userdata.txt") as file:
            file.seek(0)
            for line in file:
                lst = line.split()
                data = {
                    "firstname": lst[0],
                    "Lastname": lst[1],
                    "username": lst[2],
                    "password": lst[-1],
                }
                users.append(data)

    except FileNotFoundError:
        with open("userdata.txt", "w") as new_file:
            new_file.write("")

    choice = int(input("Enter your choice(1/2/3):"))
    if choice == 2:
        signup(users)
    elif choice == 1:
        username = input("Enter your username:")
        password = input("Enter password:")
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Account login successfully.")
                with open(f"{user['username']}_history.txt", "a") as history_file:
                    history_file.write("")
                options_func(username, fast_food_menu, cart)
                break
        else:
            print("Account not found,please create one.")
    elif choice == 3:
        break
    else:
        print("Choice is not valid.")
