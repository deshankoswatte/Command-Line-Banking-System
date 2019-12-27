from Account import Account

# Deshan Koswatte
# 2016198

print("=====================================")
print("Done by = Dehami Deshan Koswatte")
print("Student ID = 2016198")

set_of_accounts = set()


def create_account():
    print("Choice number 1 is selected by the customer\n")

    if len(set_of_accounts) < 10:
        name = str(input("Input Fullname : "))
        pin = str(input("Please input a pin of your choice : "))
        balance = eval(input("Please input a amount to deposit to start an account : "))

        account = Account(name, pin, balance)
        set_of_accounts.add(account)

        print("\n----New account created successfully !----")
        print("Note! Please remember the Name and Pin")
        print("========================================")

    else:
        print("\nCustomer registration exceed reached the no:of spaces left are: " + str((len(set_of_accounts)) - 10))

    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def withdraw():
    print("Choice number 2 is selected by the customer\n")

    available = False

    name = input("Please input name : ")
    pin = input("Please input pin : ")
    # This while loop will prevent the user using the account if the username or pin is wrong.
    for account in set_of_accounts:
        if account.__get_name__() == name and account.pin == pin:
            available = True
            # These few statement would show the balance taken from the list.
            print("Your Current Balance: " + str(account.__get_balance__()) + "-/Rs\n")
            balance = (account.__get_balance__())
            # Statement below would take the amount to withdraw from user.
            withdrawal = eval(input("Input amount to Withdraw : "))
            # The if condition below would look whether the withdraw is greater than the balance.
            if withdrawal > balance:
                # This statement below would take a deposition from the customer.
                deposition = eval(input("Please Deposit a higher Value because your Balance "
                                        "mentioned above is not enough : "))
                # These few statements would update the value and show the balance to user.
                balance = balance + deposition
                print("Your Current Balance: " + str(balance) + " -/Rs\n")
                balance = balance - withdrawal

                print("\n----Withdraw Successful!----")
                account.__set_balance__(balance)
                print("Your New Balance: " + str(balance) + " -/Rs\n\n")
            else:
                # Else condition mentioned above is to do withdrawal if the balance is greater than the
                # withdraw amount.
                balance = balance - withdrawal
                # These few statement would update the values in the list and show it to the customer.
                print("\n----Withdraw Successful!----")
                account.__set_balance__(balance)
                print("Your New Balance: " + str(balance) + " -/Rs\n\n")
    if not available:
        # The if condition above would work when the pin or the name is wrong.
        print("Your name and pin does not match!\n")

        # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def deposit():
    print("Choice number 3 is selected by the customer\n")

    available = False

    name = input("Please input name : ")
    pin = input("Please input pin : ")
    # The while loop below would work when the pin or the username is wrong.
    for account in set_of_accounts:
        if account.__get_name__() == name and account.pin == pin:
            available = True
            # These statements below would show the customer balance and update list values according to
            # the deposition made.
            print("Your Current Balance: " + str(account.__get_balance__()) + " -/Rs")
            balance = account.__get_balance__()
            # This statement below takes the deposition from the customer.
            deposition = eval(input("Enter the value you want to deposit : "))
            balance = balance + deposition
            account.__set_balance__(balance)
            print("\n----Deposition successful!----")
            print("Your New Balance: " + str(balance) + " -/Rs\n\n")

    if not available:
        print("Your name and pin does not match!\n")
    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def print_all_customers():
    print("Choice number 4 is selected by the customer\n")
    print("Customer name list and balances mentioned below : \n")

    if len(set_of_accounts) > 0:
        # The while loop below will keeping running until all the customers and balances are shown.
        for account in set_of_accounts:
            print("->. Customer = " + str(account.__get_name__()))
            print("->. Balance = " + str(account.__get_balance__()) + " -/Rs\n")
            # This statement below helps the user to go back to the start of the program (main menu).
    else:
        print("No accounts are persisted yet.\n")
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def exit_program():
    # These statements would be just showed to the customer.
    print("Choice number 5 is selected by the customer")
    print("Thank you for using our banking system!\n")
    print("Come again")
    print("Bye bye")


def invalid_function():
    print("Invalid option selected by the customer")
    print("Please Try again!\n")
    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


# This statement below helps the program to run continuously.
while True:
    # os.system("cls")
    print("")
    print("=====================================")
    print(" ----Welcome to Times Bank----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        # This function will open a new account.
        create_account()
    elif choiceNumber == "2":
        # This function will withdraw money from a specific account.
        withdraw()
    elif choiceNumber == "3":
        # This function will deposit money to a specific account.
        deposit()
    elif choiceNumber == "4":
        # This function will print all the available customers.
        print_all_customers()
    elif choiceNumber == "5":
        # This function is the point of exit from the program.
        exit_program()
        break
    else:
        # This else function above would work when a wrong function is chosen.
        invalid_function()
