import time


def signup(users):
    with open("userdata.txt", "a") as f:
        firstname = input("Enter your 1st name:").replace(" ", "")
        if firstname == "":
            while True:
                print("It should not ne empty,rewrite it!!.")
                firstname = input("Enter your 1st name:").replace(" ", "")
                if firstname != "":
                    break
        lastname = input("Enter your last name:").replace(" ", "")
        if lastname == "":
            while True:
                print("It should not ne empty,rewrite it!!.")
                lastname = input("Enter your last name:").replace(" ", "")
                if lastname != "":
                    break
        username = input("Enter your username(Without any space's):")
        password = input("Set a password(Atleast 7 characters):")
        if len(password) < 7:
            while True:
                print("Password length should be atleast 7 digits.")
                password = input("Set a password(Atleast 7 characters):")
                if len(password) >= 7:
                    break

        for user in users:
            if user["username"] == username:
                print("Username already exist,login or create a new account.")
                break
        else:
            f.write(f"{firstname} {lastname} {username} {password}\n")
            print("Your account is created login to continue.")


def options_func(username, fast_food_menu, cart):
    while True:
        options = "\n1. View Menu\n2. Add products to cart\n3. Remove products from cart\n4. View cart\n5. View shopping history\n6. Checkout\n7. Move to Home Page\n"
        print(options)
        option = int(input("Select Any Option Mentioned Above:"))
        if option == 1:
            print("Welcome!!!,We Offer Following Saviour's:")
            for key, val in fast_food_menu.items():
                print(key, val)
        elif option == 2:
            selection = input("Select any item from menu:")
            if selection in fast_food_menu:
                try:
                    quantity = int(input("How Many:"))
                except:
                    print("Quantity should be numeric.")
                    quantity = int(input("How Many:"))
                if quantity < 0:
                    print("Quantity should be a positive number,add item again.")
                else:
                    price = quantity * fast_food_menu[selection]["price"]
                    cart[selection] = price
                    want_more(fast_food_menu, cart)
            else:
                print("Item not available,check menu.")
        elif option == 3:
            to_remove = input("What you want to remove from cart?:")
            if to_remove in cart:
                quantity = int(input("How Many:"))
                if quantity * fast_food_menu[to_remove]["price"] == cart[to_remove]:
                    cart.pop(to_remove)
                    print(f"{to_remove} is being removed from cart.")
                elif quantity * fast_food_menu[to_remove]["price"] < cart[to_remove]:
                    cart[to_remove] = (
                        cart[to_remove] - quantity * fast_food_menu[to_remove]["price"]
                    )
                    print(f"{quantity} {to_remove} is being removed from cart.")
                else:
                    print("You enter quantity greater than the existing one,view cart.")
            else:
                print("Item is already not present there.")
        elif option == 4:
            if cart:
                print(f"Your cart is:")
                for key, val in cart.items():
                    items = val / (fast_food_menu[key]["price"])
                    print(f"{key.capitalize()} ({items} items) :${val}")
            else:
                print("Cart is empty,add products first.")
        elif option == 5:
            view_history(username)
        elif option == 6:
            if cart:
                address = input("Enter your current address:")
                values = []
                for i in cart.values():
                    values.append(i)
                total = sum(values)
                print(f"Your cart is:{cart}\nYour total bill is:{total}")
                print(
                    f"Thanks for shopping!!!\nYour order will be delivered to {address} in 30 minutes."
                )
                save_history(username, cart)
                cart.clear()
            else:
                print("Your cart is empty,please select some items first.")

        elif option == 7:
            print("Welcome To QuickBite Express\n1. LOGIN\n2. SIGNUP\n3. EXIT")
            break


def want_more(fast_food_menu, cart):
    while True:
        decision = input("Do you want to add other item's(Y/N):")
        if decision == "n" or decision == "N":
            break
        elif decision == "Y" or decision == "y":
            order(fast_food_menu, cart)


def order(fast_food_menu, cart):
    selection = input("What do you want?:")
    if selection in fast_food_menu:
        try:
            quantity = int(input("How Many:"))
        except:
            print("Quantity should be numeric.")
            quantity = int(input("How Many:"))
        if quantity < 0:
            print("Quantity should be a positive number,add item again.")
        else:
            price = quantity * fast_food_menu[selection]["price"]
            cart[selection] = price
    else:
        print("Item not available,check menu.")


def save_history(username, cart):
    order_time = time.ctime(time.time())
    with open(f"{username}_history.txt", "a") as f:
        f.write(f"Order Details: {cart} | {order_time}\n")


def view_history(username):
    with open(f"{username}_history.txt", "r") as f:
        content = f.read()
        if content:
            print(f"Order History for {username}:\n{content}")
        else:
            print(f"No order history found for {username}.")
