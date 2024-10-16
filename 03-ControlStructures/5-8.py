while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. check password")
    print("5. change password")
    print("6. Exit")
    pin = 1234
    balance = 4000
    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        newpin= input('enter your new password:')
        if newpin.isdigit()==True:
            print('your pin is changed')
        else:
            print('your pin is incorrect')
    elif choice =="4":
        print(f'your pin is {pin}')

    else:
        print("Invalid option. Please try again.")
