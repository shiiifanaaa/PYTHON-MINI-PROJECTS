
# Smart Banking System

correct_pin = 1234
balance = 10000
attempts = 0
max_attempts = 3
transactions = 0

print("===== WELCOME TO SMART BANKING =====")

# Login system

while attempts < max_attempts:

    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("\nLogin Successful!")
        break

    else:
        attempts += 1
        print("Incorrect PIN!")
        print("Attempts remaining:", max_attempts - attempts)

if attempts == max_attempts:
    print("Account Locked!")

else:

    # Banking menu

    while True:

        print("\n===== BANKING MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction Count")
        print("5. Future Feature")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("Available Balance: ₹", balance)

        elif choice == 2:

            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount!")
                continue

            balance += amount
            transactions += 1

            print("Deposit Successful!")
            print("New Balance: ₹", balance)

        elif choice == 3:

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount!")
                continue

            if amount > balance:
                print("Insufficient Balance!")
                continue

            balance -= amount
            transactions += 1

            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", balance)

        elif choice == 4:

            print("Total Transactions:", transactions)

        elif choice == 5:

            print("This feature is under development.")
            pass

        elif choice == 6:

            print("Thank you for using Smart Banking!")
            break

        else:

            print("Invalid choice!")
            continue
