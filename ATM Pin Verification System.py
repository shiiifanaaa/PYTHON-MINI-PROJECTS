secret_pin = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    pin = int(input("Enter your ATM PIN: "))

    if pin == secret_pin:
        print("Access Granted!")
        print("Welcome to your ATM account.")
        break

    else:
        attempts += 1
        print("Incorrect PIN!")

        print("Attempts remaining:", max_attempts - attempts)

if attempts == max_attempts:
    print("Account Locked!")
