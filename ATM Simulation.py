print("====== WELCOME TO ATM ======")

correct_pin = 1234
balance = 10000

pin = int(input("Enter your ATM PIN: "))

if pin == correct_pin:

    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount <= balance:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Remaining balance: Rs.", balance)

        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Updated balance: Rs.", balance)

        else:
            print("Invalid deposit amount")

    elif choice == 4:
        print("Thank you for using our ATM!")

    else:
        print("Invalid choice")

else:
    print("Incorrect PIN. Access denied.")

print("\n====== THANK YOU ======")
