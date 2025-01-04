import os
import getpass

# Function to load existing users from the file
def load_users():
    if not os.path.exists("users.txt"):
        open("users.txt", "w").close()  # Create the file if it doesn't exist
    with open("users.txt", "r") as file:
        users = file.readlines()
    return [user.strip().split(",")[0] for user in users]  # Return only usernames

# Function to register a new user
def register():
    print("\n=== Register ===")
    username = input("Enter a new username: ")
    if username in load_users():
        print("Username already exists. Try a different one.")
        return
    password = getpass.getpass("Enter a new password: ")
    confirm_password = getpass.getpass("Confirm your password: ")
    
    if password != confirm_password:
        print("Passwords do not match. Try again.")
        return

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")

# Function to login a user
def login():
    print("\n=== Login ===")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    with open("users.txt", "r") as file:
        users = file.readlines()
    
    for user in users:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and password == stored_password:
            print("Login successful!")
            return username  # Return username to identify the logged-in user
    print("Invalid credentials. Try again.")
    return None

# Function to unregister a user
def unregister():
    print("\n=== Unregister ===")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    with open("users.txt", "r") as file:
        users = file.readlines()
    
    updated_users = []
    for user in users:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and password == stored_password:
            print("Account successfully deleted.")
        else:
            updated_users.append(user)  # Keep all other users

    # Write updated user list back to the file
    with open("users.txt", "w") as file:
        file.writelines(updated_users)

# Function for the to-do list
def to_do_list():
    print("\n=== To-Do List ===")
    to_do = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Logout")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter a task: ")
            to_do.append(task)
            print("Task added!")
        elif choice == "2":
            print("\nYour Tasks:")
            for idx, task in enumerate(to_do, start=1):
                print(f"{idx}. {task}")
        elif choice == "3":
            task_num = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_num < len(to_do):
                removed_task = to_do.pop(task_num)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid option. Try again.")

# Function to display registered users
def display_users():
    users = load_users()
    if users:
        print("\n=== Registered Users ===")
        for idx, user in enumerate(users, start=1):
            print(f"{idx}. {user}")
    else:
        print("\nNo users registered yet.")

# Main program
while True:
    print("\nWelcome to Asha's To-do list")
    print("1. View Registered Users\n2. Register\n3. Login\n4. Unregister\n5. Exit")
    option = input("Choose an option: ")
    
    if option == "1":
        display_users()
    elif option == "2":
        register()
    elif option == "3":
        logged_in_user = login()
        if logged_in_user:
            to_do_list()
    elif option == "4":
        unregister()
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
