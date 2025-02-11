import csv
import os

ACCOUNT_FILE = 'account_details.csv'
TRANSACTION_FILE = 'transactions.csv'


def initialize_csv():
    if not os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Account Number", "Name", "Current Balance"])

    if not os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Account Number", "Transaction Type", "Amount"])


def create_account(name, amount):
    try:
        with open(ACCOUNT_FILE, "r") as f:
            rows = list(csv.reader(f))
            last_row = rows[-1] if len(rows) > 1 else None

        account_number = int(last_row[0]) + 1 if last_row else 10001
    except (ValueError, IndexError):
        account_number = 10001

    with open(ACCOUNT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account_number, name, amount])

    with open(TRANSACTION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account_number, "Deposit", amount])
    return account_number


def statement(account_number):
    with open(TRANSACTION_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)
        print(f"Statement for Account {account_number}:")
        for row in reader:
            if int(row[0]) == account_number:
                print(f"Type: {row[1]}, Amount: {row[2]}")


def verify_user(account_number):
    with open(ACCOUNT_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if int(row[0]) == account_number:
                return {"name": row[1], "current_balance": float(row[2])}
    return None


def update_current_balance(account_number, amount):
    rows = []
    with open(ACCOUNT_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(account_number):
                row[2] = str(float(row[2]) + amount)
            rows.append(row)

    with open(ACCOUNT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def deposit(account_number, amount):
    if amount <= 0:
        print("Amount should be greater than zero.")
        return
    with open(TRANSACTION_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account_number, "Deposit", amount])
    update_current_balance(account_number, amount)
    print("Deposit successful!")


def withdrawal(account_number, amount):
    if amount <= 0:
        print("Amount should be greater than zero.")
        return
    user = verify_user(account_number)
    if user and user["current_balance"] >= amount:
        with open(TRANSACTION_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([account_number, "Withdrawal", amount])
        update_current_balance(account_number, -amount)
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")


def menu(acc):
    while True:
        user = verify_user(acc)
        if user:
            print(f"Welcome {user['name']}, Your Current Balance is Rs {user['current_balance']}")
            print('''
            1. Deposit
            2. Withdrawal
            3. Statement
            4. Exit
            ''')
            choice = input("Enter choice: ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                deposit(acc, amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                withdrawal(acc, amount)
            elif choice == '3':
                statement(acc)
            elif choice == '4':
                print("Thank you for using our banking service!")
                break
            else:
                print("Invalid choice. Try again.")
        else:
            print("Account not found!")
            return


if __name__ == "__main__":
    initialize_csv()
    print('''
    Enter:
    1. Create new account
    2. To go to banking services
    ''')
    ch = input("Enter: ")
    if ch == '1':
        name = input("Name: ")
        balance = float(input("Amount: "))
        new_account_number = create_account(name, balance)
        print(f"Your new account number: {new_account_number}")
    elif ch == '2':
        account_number = int(input("Enter account number: "))
        menu(account_number)
    else:
        print("Invalid choice!")
