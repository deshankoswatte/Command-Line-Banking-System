#Deshan Koswatte
#2016198
import os
print("=====================================")
print("Done by = Dehami Deshan Koswatte")
print("Student ID = 2016198")
customernames=['Jane Smith','Iason Jordan','David Morgan','Brain John','Jack Swift']
customerpins=['0123','2575','7275','2312','5049']
customerbalance=[10000,20000,20000,40000,10000]
Deposit=0
Withdraw=0
Balance=0
count=1
count2=5
i=0
#This statement below helps the program to run continuosly.
while True:
    #os.system("cls")
    print("=====================================")
    print(" ----Welcome to Times Bank----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")
    #The below statement takes the choice number from the user.
    Choiceno=input("Select your choice number from the above menu : ")
    if(Choiceno=="1"):
        print ("Choice number 1 is selected by the customer")
        #The line below will take the no:of customers from the user.
        NOC=eval(input("Number of Customers : "))
        i=i+NOC
        #The if condition will restrict the number of new account to 5.
        if(i>5):
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i=i-NOC
        else:
            #The while loop will run according to the no:of customers.
            while(count<=i):
                #These few lines will take information from customer and then append them to the list.
                Name=input("Input Fullname : ")
                customernames.append(Name)
                Pin=str(input("Please input a pin of your choice : "))
                customerpins.append(Pin)
                Balance=0
                Deposit=eval(input("Please input a value to deposit to start an account : "))
                Balance=Balance+Deposit
                customerbalance.append(Balance)
                print("\nName=",end=" ")
                print(customernames[count2])
                print("Pin=",end=" ")
                print(customerpins[count2])
                print("Balance=",end=" ")
                print(customerbalance[count2],end=" ")
                print("-/Rs")
                count=count+1
                count2=count2+1
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customernames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
                #This statement below helps the user to go back to the start of the program (main menu).
        Mainmenu=input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif(Choiceno=="2"):
        J=0
        print ("Choice number 2 is selected by the customer")
        #This while loop will prevent the user using the account if the username or pin is wrong.
        while(J<1):
            k=-1
            Name=input("Please input name : ")
            Pin=input("Please input pin : ")
            #This while loop will keep the function running when variable k is smaller than length of the customernames list.
            while(k<len(customernames)-1):
                k=k+1
                #These two if conditions find where both the name and pin matches.
                if(Name==customernames[k]):
                    if(Pin==customerpins[k]):
                        J=J+1
                        #These few statement would show the balance taken from the list.
                        print("Your Current Balance:",end=" ")
                        print(customerbalance[k],end=" ")
                        print("-/Rs\n")
                        Balance=(customerbalance[k])
                        #Statement below would take the amount to withdraw from user.
                        Withdraw=eval(input("Input value to Withdraw : "))
                        #The if condition below would look whether the withdraw is greater than the balance.
                        if(Withdraw>Balance):
                            #This statement below would take a deposition from the customer.
                            Deposit=eval(input("Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            #These few statements would update the value and show the balance to user.
                            Balance=Balance+Deposit
                            print("Your Current Balance:",end=" ")
                            print(Balance,end=" ")
                            print("-/Rs\n")
                            Balance=Balance-Withdraw
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerbalance[k]=Balance
                            print("Your New Balance: ",Balance,end=" ")
                            print("-/Rs\n\n")
                        else:
                            #Else condition mentioned above is to do withdrawal if the balance is greater than the withdraw amount.
                            Balance=Balance-Withdraw
                            #These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerbalance[k]=Balance
                            print("Your New Balance: ",Balance,end=" ")
                            print("-/Rs\n\n")
            if(J<1):
                #The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
            #This statement below helps the user to go back to the start of the program (main menu).
        Mainmenu=input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif(Choiceno=="3"):
        print("Choice number 3 is selected by the customer")
        N=0
        #The while loop below would work when the pin or the username is wrong.
        while(N<1):
            k=-1
            Name=input("Please input name : ")
            Pin=input("Please input pin : ")
            #The while loop below will keep the function running to find the correct user.
            while(k<len(customernames)-1):
                k=k+1
                #The two if conditions below would find whether both the pin and the name is correct.
                if(Name==customernames[k]):
                    if(Pin==customerpins[k]):
                        N=N+1
                        #These statements below would show the customer balance and update list values according to the deposition made.
                        print("Your Current Balance: ",end=" ")
                        print(customerbalance[k],end=" ")
                        print("-/Rs")
                        Balance=(customerbalance[k])
                        #This statement below takes the depositionn from the customer.
                        Deposit=eval(input("Enter the value you want to deposit : "))
                        Balance=Balance+Deposit
                        customerbalance[k]=Balance
                        print("\n")
                        print("----Deposit successfull!----")
                        print("Your New Balance: ",Balance,end=" ")
                        print("-/Rs\n\n")
            if(N<1):
                print("Your name and pin does not match!\n")
                break
            #This statement below helps the user to go back to the start of the program (main menu).
        Mainmenu=input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif(Choiceno=="4"):
        print("Choice number 4 is selected by the customer")
        k=0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        #The while loop below will keeping running until all the customers and balances are shown.
        while(k<=len(customernames)-1):
            print("->.Customer =",customernames[k])
            print("->.Balance =",customerbalance[k],end=" ")
            print("-/Rs")
            print("\n")
            k=k+1
            #This statement below helps the user to go back to the start of the program (main menu).
        Mainmenu=input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif(Choiceno=="5"):
        #These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print ("Bye bye")
        break
    else:
        #This else function above would work when a wrong function is choosed.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        #This statement below helps the user to go back to the start of the program (main menu).
        Mainmenu=input("Please press enter key to go back to main menu to perform another function or exit ...")
