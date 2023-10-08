# =============================================================
# == Author : <Muhammad Taha Khurram>
# == Date   :  <October, 7th 2023>
# == Desc   :  <CLI Airplane management system>
# == Roll No. : <261-905060>
# =============================================================

# Implement user and admin login

# Screen 1 => Login Screen.
# Screen 2 => Menu for user
# Screen 3 => UI (Menu for user)
# Screen 4 => Pag to select flights'
# Screen 5 => Seat Availability plan
# Screen 6 => Confirmation of seat and saving in a txt file -> User can again cancel th seat which should be updated
# Screen 7 => Menu for admin


# Storing data files
# Users (directory)
# Flights (directory)
# UserSeats (directory)
import os

import os


def usrMenu():
    while True:
        print(f"Welcome user!")
        print("\t 1.Book a ticket")
        print("\t 2.Cancel a booking")
        print("\t 3.Show flights")

        choice = input("Please enter your choice: ")

        if choice == "1":
            bookingTicket()
        elif choice == "2":
            print("You selected Option 2")
        elif choice == "3":
            print("You selected Option 3")
        exit_choice = input("Enter 'exit' to quit or press Enter to continue: ")
        if exit_choice.lower() == 'exit':
            break


def bookingTicket():
    while True:
        print(f"Welcome user!")
        print("\t 1.Book a ticket")
        print("\t 2.Cancel a booking")
        print("\t 3.Show flights")
        print("\t 4.<= Go Back")

        choice = input("Enter the corresponding number: ")

        if choice == "1":
            print("You selected Option 1")
        elif choice == "2":
            print("You selected Option 2")
        elif choice == "3":
            print("You selected Option 3")
        elif choice == "4":
            usrMenu()
        else:
            print("Please select right option")


def adminMenu():
    while True:
        print(f"Welcome admin!")
        print("\t 1.Add a flight")
        print("\t 2.Modify a flight")
        print("\t 3.Remove a flight")
        print("\t 4.Show flights")

        usrchoice = input("Please enter your choice: ")

        if usrchoice == "1":
            addFlight()
        elif usrchoice == "2":
            print(loadFlight())
        elif usrchoice == "3":
            removeFlight()
        elif usrchoice == "4":
            print(loadFlight())
        exit_choice = input("Enter 'exit' to quit or press Enter to continue: ")
        if exit_choice.lower() == 'exit':
            break


def addFlight():
    flight_name = input("Enter flight name: ")
    num_rows = int(input("Enter number of rows: "))
    num_cols = int(input("Enter number of columns: "))
    seats = [[True for _ in range(num_cols)] for _ in range(num_rows)]  # True represents available seats

    # Directory to store flight data
    flight_directory = os.path.join(os.getcwd(), "Flights")
    if not os.path.exists(flight_directory):
        os.mkdir(flight_directory)

    # Filepath to store flight information
    filepath = os.path.join(flight_directory, f"{flight_name}.txt")

    try:
        with open(filepath, "w") as file:
            file.write(f"Flight Name: {flight_name}\n")
            file.write(f"Number of Rows: {num_rows}\n")
            file.write(f"Number of Columns: {num_cols}\n")
            for row in seats:
                file.write(" ".join(str(int(seat)) for seat in row) + "\n")
        print(f"Flight '{flight_name}' created with {num_rows} rows and {num_cols} columns.")
        adminMenu()
    except IOError:
        print("Error occurred while saving flight data.")


def loadFlight():
    flights = {}
    flight_directory = os.path.join(os.getcwd(), "Flights")
    if os.path.exists(flight_directory):
        flight_files = os.listdir(flight_directory)
        flight_names = [filename.rstrip('.txt') for filename in flight_files]

        # Print available flight names
        print("Available Flights:")
        for index, flight_name in enumerate(flight_names, start=1):
            print(f"{index}. {flight_name}")

        # Ask the user to select a flight
        selected_index = int(input("Enter the number of the flight you want to load: ")) - 1

        if 0 <= selected_index < len(flight_files):
            selected_flight_filename = flight_files[selected_index]
            with open(os.path.join(flight_directory, selected_flight_filename), "r") as file:
                lines = file.readlines()
                flight_name = lines[0].split(":")[1].strip()
                num_rows = int(lines[1].split(":")[1].strip())
                num_cols = int(lines[2].split(":")[1].strip())
                seats = [[bool(int(seat)) for seat in row.split()] for row in lines[3:]]
                flights[flight_name] = {"num_rows": num_rows, "num_cols": num_cols, "seats": seats}
                display_flight_seats(seats)  # Assuming you have a function to display seats
        else:
            print("Invalid selection. Please try again.")

        print("Press 1 to go back")
        print("Press 2 to load another flight")

        usrchoice = input("Please enter your choice: ")

        if usrchoice == "1":
            adminMenu()
        elif usrchoice == "2":
            loadFlight()


def removeFlight():
    flights = {}
    flight_directory = os.path.join(os.getcwd(), "Flights")
    if os.path.exists(flight_directory):
        flight_files = os.listdir(flight_directory)
        flight_names = [filename.rstrip('.txt') for filename in flight_files]

        # Print available flight names
        print("Available Flights:")
        for index, flight_name in enumerate(flight_names, start=1):
            print(f"{index}. {flight_name}")

        # Ask the user to select a flight
        selected_index = int(input("Enter the number of the flight you want to load: ")) - 1

        if 0 <= selected_index < len(flight_files):
            selected_flight_filename = flight_files[selected_index]
            file_path = os.path.join(flight_directory, selected_flight_filename)

            # Remove the selected flight file
            os.remove(file_path)

            print(f"Flight '{selected_flight_filename.rstrip('.txt')}' removed successfully.")
        else:
            print("Invalid selection. Please try again.")

        print("Press 1 to go back")
        print("Press 2 to load another flight")

        usrchoice = input("Please enter your choice: ")

        if usrchoice == "1":
            adminMenu()
        elif usrchoice == "2":
            loadFlight()


def display_flight_seats(flight):
    print("\t\t\t", end="")
    for i in range(len(flight[0])):
        print(chr(65 + i), end="   ")
    print()

    for i, row in enumerate(flight):
        print("Row " + str(i + 1) + ".", end="   ")
        for seat in row:
            print("*" if seat else "x", end="   ")
        print()


def loginVerify(username, password):
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "Users"
    filepath = os.path.join(here, subdir)

    if username in os.listdir(filepath):  # Check if the username file exists
        try:
            with open(os.path.join(filepath, username), 'r') as file:
                stored_username = file.readline().strip()
                stored_password = file.readline().strip()
                stored_role = file.readline().strip()

                # Verify the provided username and password
                if stored_username == "Username: " + username and stored_password == "Password: " + password:
                    if stored_role == "Role: 1":
                        return "user"
                    elif stored_role == "Role: 2":
                        return "admin"
                    else:
                        return "Error occurred while reading role data."
                else:
                    return "Incorrect Password"
        except IOError:
            return "Error occurred while reading user data."
    else:
        return "Incorrect Username"


def UsrRegister(username, password, role):
    role = role.lower()
    if role == "user":
        usrRole = "1"
    elif role == "admin":
        usrRole = "2"
    else:
        return "Incorrect role provided"

    # Check if the Users directory exists, create it if not
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "Users"
    filepath = os.path.join(here, subdir)

    files = os.listdir()
    if subdir in files:
        pass
    else:
        os.mkdir(os.path.join(here, subdir))

    # Check if the username already exists
    if os.path.isfile(os.path.join(filepath, username)):
        return "Username already exists. Please choose a different username."
    else:
        try:
            # Open the file in write mode and write username and password
            with open(os.path.join(filepath, username), 'w') as f:
                f.write("Username: " + username + "\n")
                f.write("Password: " + password + "\n")
                f.write("Role: " + usrRole)
            return "User has been registered successfully!"
        except IOError:
            return "Error occurred while registering the user. Please try again later."


def loginFunction():
    while True:
        usrInput = input("Enter your username: ")
        passwordInput = input("Enter your password: ")
        returnMsg = loginVerify(usrInput, passwordInput)

        if returnMsg == "user":
            return "user"
        elif returnMsg == "admin":
            return "admin"
        else:
            print(returnMsg)

        exit_choice = input("Enter 'exit' to quit or press Enter to continue: ")
        if exit_choice.lower() == 'exit':
            break


def main():
    print("====== AIRPLANE MANAGEMENT SYSTEM ======")
    # print(UsrRegister("admin", "123", "admin"))
    returnLogin = loginFunction()
    if returnLogin == "user":
        usrMenu()
    elif returnLogin == "admin":
        adminMenu()
    else:
        "Error occurred"
    # print(UsrRegister(usrInput, passwordInput, "user"))


if __name__ == '__main__':
    main()
