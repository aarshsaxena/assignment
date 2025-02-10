class Bank:
    __account=100000000000
    def __init__(self,name:str,balance:int):
        Bank.__account+=1
        self.account_number=Bank.__account
        self.name=name
        self.balance=balance
        self.transaction=[]
        self.transaction.append(("Deposit",self.balance))
        print(f"Successfully created A/c {self.account_number} with Rs {self.balance}/-")

    def deposit(self,amount:int):
        if amount<=0:
            print("Amount should be greater than zero.")
            return

        else:
               self.balance+=amount
               self.transaction.append(("Deposit",amount))
               print(f"Deposited Rs {amount}/- successfully.")

    def withdrawal(self,amount:int):
        if amount>self.balance:
            print("Insufficient Balance!")
            return

        elif amount<=0:
            print("Amount should be greater than zero.")
            return

        else:
            self.balance-=amount
            self.transaction.append(("Withdrawal",amount))
            print(f"Withdrawal Rs {amount}/- successfully.")

    def statement(self):
        print(f"\n\nAccount Statement of A/c {self.account_number} -- Current Balance: Rs {self.balance}/-")
        for i in self.transaction:
            print(f"{i[0]} Rs {i[1]}/-")


if __name__=="__main__":
    alice=Bank("Alice",100)
    bob=Bank("Bob",250)

    alice.deposit(200)
    alice.deposit(150)
    alice.deposit(-12)
    bob.withdrawal(0)
    bob.withdrawal(150)
    bob.withdrawal(150)
    bob.deposit(200)
    alice.withdrawal(50)

    alice.statement()
    bob.statement()
