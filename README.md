
Simple Login and To-Do List App

A Python-based console application that combines a **user login system** with a simple **to-do list manager**. The project supports **user registration**, **login**, **account management (unregister)**, and a personalized to-do list. This application is beginner-friendly and demonstrates basic file handling and user authentication in Python.


Features

1. **User Registration**
   - Create a new account with a unique username and password.
   - Passwords are securely entered (hidden input during typing).

2. **User Login**
   - Authenticate with your username and password.
   - Access your personal to-do list after logging in.

3. **Unregister (Delete Account)**
   - Delete your account by providing the correct username and password.

4. **To-Do List Management**
   - Add tasks to your personal to-do list.
   - View your current tasks.
   - Remove tasks by their position in the list.

5. **View Registered Users**
   - See a list of all registered usernames (admin-level feature).

---

## How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Run the Program**
   Ensure Python 3.x is installed on your system, then run:
   ```bash
   python main.py
   ```

---

## Files

- **`main.py`**: The main Python script that runs the application.
- **`users.txt`**: Stores user credentials in the format `username,password`. Automatically created if it doesn't exist.

---

## Usage

### Main Menu Options
1. **View Registered Users**  
   Displays a list of all registered usernames.
   
2. **Register**  
   Register a new account with a unique username and password.

3. **Login**  
   Log in with your credentials to access the to-do list.

4. **Unregister**  
   Permanently delete your account (username and password required).

5. **Exit**  
   Close the application.

### To-Do List Options (After Login)
1. **Add Task**  
   Add a task to your personal to-do list.

2. **View Tasks**  
   Display all tasks in your to-do list.

3. **Remove Task**  
   Remove a specific task by its number.

4. **Logout**  
   Exit the to-do list and return to the main menu.

---

## Example Workflow

1. Register a new user:
   ```
   Enter a new username: john_doe
   Enter a new password: *****
   Confirm your password: *****
   Registration successful!
   ```

2. Login:
   ```
   Enter your username: john_doe
   Enter your password: *****
   Login successful!
   ```

3. Add tasks to the to-do list:
   ```
   1. Add Task
   Enter a task: Complete Python project
   Task added!
   ```

4. View tasks:
   ```
   1. Complete Python project
   ```

5. Remove a task:
   ```
   Enter the task number to remove: 1
   Removed task: Complete Python project
   ```

6. Unregister your account:
   ```
   Enter your username: john_doe
   Enter your password: *****
   Account successfully deleted.
   ```

---

## Requirements

- Python 3.x


---

## Contributions

Feel free to contribute to this project by submitting a pull request. If you encounter any issues or have feature suggestions, please open an issue in the repository.

---

## Author

Developed by Asha V K R
GitHub: [[https://github.com/<your-username>](https://github.com/<](https://github.com/aasharaaj)
