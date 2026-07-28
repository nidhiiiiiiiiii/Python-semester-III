# Login status and call count
logged_in = False
call_count = 0


# 1. Login authentication decorator
def login_required(function):

    def wrapper():

        if logged_in == True:
            function()
        else:
            print("Access denied. Please log in first.")

    return wrapper


# 2. Function call logger decorator
def log_call(function):

    def wrapper():

        time = input("Enter the current time: ")

        print("The function was called at:", time)

        function()

    return wrapper

# 3. Input validation decorator
def validate_numbers(function):

    def wrapper(number1, number2):

        if number1 > 0 and number2 > 0:
            function(number1, number2)
        else:
            print("Error: Please enter positive integers only.")

    return wrapper

# 4. Function call counter decorator
def count_calls(function):

    def wrapper():

        global call_count

        call_count = call_count + 1

        print("The function has been called", call_count, "time(s).")

        function()

    return wrapper

# Protected function
@login_required
def view_profile():

    print("Welcome to your profile!")

# Function with call logger
@log_call
def display_message():

    print("This is a logged function.")


# Function with input validation
@validate_numbers
def add_numbers(number1, number2):

    answer = number1 + number2

    print("Answer:", answer)


# Function with call counter
@count_calls
def say_hello():

    print("Hello!")


# Main program
while True:

    print("\n===== MAIN MENU =====")
    print("1. Login")
    print("2. Logout")
    print("3. View Profile")
    print("4. Function Logger")
    print("5. Add Two Numbers")
    print("6. Call Counter")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        logged_in = True
        print("Login successful.")

    elif choice == "2":

        logged_in = False
        print("Logout successful.")

    elif choice == "3":

        view_profile()

    elif choice == "4":

        display_message()

    elif choice == "5":

        first_input = input("Enter the first positive integer: ")
        second_input = input("Enter the second positive integer: ")

        if first_input.isdigit() and second_input.isdigit():

            number1 = int(first_input)
            number2 = int(second_input)

            add_numbers(number1, number2)

        else:
            print("Error: Please enter positive integers only.")

    elif choice == "6":

        say_hello()

    elif choice == "7":

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")