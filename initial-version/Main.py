# Deshan Koswatte
# 2016198

print("=====================================")
print("Done by = Dehami Deshan Koswatte")
print("Student ID = 2016198")

customer_names = ['Jane Smith', 'Iason Jordan', 'David Morgan', 'Brain John', 'Jack Swift']
customer_pass_codes = ['0123', '2575', '7275', '2312', '5049']
customer_balances = [10000, 20000, 20000, 40000, 10000]


def new_account():
    print("Choice number 1 is selected by the customer")

    counter_1 = 1
    counter_2 = 5
    i = len(customer_names)

    # The line below will take the no:of customers from the user.
    no_of_accounts = eval(input("Number of Accounts to be created : "))
    i = i + no_of_accounts
    # The if condition will restrict the number of new account to 5.
    if i > 10:
        print("\n")
        print("Customer registration exceed reached the no:of spaces left are: " + i)
    else:
        # The while loop will run according to the no:of customers.
        while counter_1 <= no_of_accounts:
            # These few lines will take information from customer and then append them to the list.
            name = input("Input Fullname : ")
            customer_names.append(name)
            pin = str(input("Please input a pin of your choice : "))
            customer_pass_codes.append(pin)
            balance = 0
            deposition = eval(input("Please input a value to deposit to start an account : "))
            balance = balance + deposition
            customer_balances.append(balance)
            print("\nName=", end=" ")
            print(customer_names[counter_2])
            print("Pin=", end=" ")
            print(customer_pass_codes[counter_2])
            print("Balance=", end=" ")
            print(customer_balances[counter_2], end=" ")
            print("-/Rs")
            counter_1 = counter_1 + 1
            counter_2 = counter_2 + 1
            print("\nYour name is added to customers system")
            print("Your pin is added to customer system")
            print("Your balance is added to customer system")
            print("----New account created successfully !----")
            print("\n")
            print("Your name is avalilable on the customers list now : ")
            print(customer_names)
            print("\n")
            print("Note! Please remember the Name and Pin")
            print("========================================")
            # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def withdraw():
    j = 0
    print("Choice number 2 is selected by the customer")
    # This while loop will prevent the user using the account if the username or pin is wrong.
    while j < 1:
        k = -1
        name = input("Please input name : ")
        pin = input("Please input pin : ")
        # This while loop will keep the function running when variable k is smaller than length of the
        # customer_names list.
        while k < len(customer_names) - 1:
            k = k + 1
            # These two if conditions find where both the name and pin matches.
            if name == customer_names[k]:
                if pin == customer_pass_codes[k]:
                    j = j + 1
                    # These few statement would show the balance taken from the list.
                    print("Your Current Balance:", end=" ")
                    print(customer_balances[k], end=" ")
                    print("-/Rs\n")
                    balance = (customer_balances[k])
                    # Statement below would take the amount to withdraw from user.
                    withdrawal = eval(input("Input value to Withdraw : "))
                    # The if condition below would look whether the withdraw is greater than the balance.
                    if withdrawal > balance:
                        # This statement below would take a deposition from the customer.
                        deposition = eval(input(
                            "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                        # These few statements would update the value and show the balance to user.
                        balance = balance + deposition
                        print("Your Current Balance:", end=" ")
                        print(balance, end=" ")
                        print("-/Rs\n")
                        balance = balance - withdrawal
                        print("-\n")
                        print("----Withdraw Successful!----")
                        customer_balances[k] = balance
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
                    else:
                        # Else condition mentioned above is to do withdrawal if the balance is greater than the
                        # withdraw amount.
                        balance = balance - withdrawal
                        # These few statement would update the values in the list and show it to the customer.
                        print("\n")
                        print("----Withdraw Successful!----")
                        customer_balances[k] = balance
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
        if j < 1:
            # The if condition above would work when the pin or the name is wrong.
            print("Your name and pin does not match!\n")
            break
        # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def deposit():
    print("Choice number 3 is selected by the customer")
    n = 0
    # The while loop below would work when the pin or the username is wrong.
    while n < 1:
        k = -1
        name = input("Please input name : ")
        pin = input("Please input pin : ")
        # The while loop below will keep the function running to find the correct user.
        while k < len(customer_names) - 1:
            k = k + 1
            # The two if conditions below would find whether both the pin and the name is correct.
            if name == customer_names[k]:
                if pin == customer_pass_codes[k]:
                    n = n + 1
                    # These statements below would show the customer balance and update list values according to
                    # the deposition made.
                    print("Your Current Balance: ", end=" ")
                    print(customer_balances[k], end=" ")
                    print("-/Rs")
                    balance = (customer_balances[k])
                    # This statement below takes the deposition from the customer.
                    deposition = eval(input("Enter the value you want to deposit : "))
                    balance = balance + deposition
                    customer_balances[k] = balance
                    print("\n")
                    print("----Deposition successful!----")
                    print("Your New Balance: ", balance, end=" ")
                    print("-/Rs\n\n")
        if n < 1:
            print("Your name and pin does not match!\n")
            break
        # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def print_all_customers():
    print("Choice number 4 is selected by the customer")
    k = 0
    print("Customer name list and balances mentioned below : ")
    print("\n")
    # The while loop below will keeping running until all the customers and balances are shown.
    while k <= len(customer_names) - 1:
        print("->. Customer =", customer_names[k])
        print("->. Balance =", customer_balances[k], end=" ")
        print("-/Rs")
        print("\n")
        k = k + 1
        # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def exit_program():
    # These statements would be just showed to the customer.
    print("Choice number 5 is selected by the customer")
    print("Thank you for using our banking system!")
    print("\n")
    print("Come again")
    print("Bye bye")


def invalid_function():
    print("Invalid option selected by the customer")
    print("Please Try again!")
    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


# This statement below helps the program to run continuously.
while True:
    # os.system("cls")
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
        new_account()
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
