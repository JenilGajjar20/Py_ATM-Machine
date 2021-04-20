import random


class Account:
    # Construct an account object
    def __init__(self, id, balance = 0, annualInterestRate = 3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getMonthlyInterest(self):
        return self.balance * self.getAnnualInterestRate()


def main():
    # Creating accounts     
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

    # ATM processes
    while True:
        # Reading id from user
        id = int(input("Enter your pin: "))
        
        # Loop till id is valid        
        while id < 1000 or id > 9999:
            id = int(input("Invalid id...! Re-enter: "))

            # Iterating over account session
            while True:
                # Printing options
                print("\t1. Balance \t2. Withdraw amount \t3. Deposit amount \t4. Exit")
                
                # Reading options
                option = int(input("Enter your choice: "))

                # Getting account object     
                for acc in accounts:
                    # Comparing account id
                    if acc.getId() == id:
                        accountObj = acc
                        break

                # View Balance
                if option == 1:
                    # Printing balance
                    print(f"Your current balance is: {accountObj.getBalance()}")

                # Withdraw
                elif option == 2:
                    # Reading amount
                    withdrawAmount = float(input("Enter your amount to withdraw: "))
                    verifyWithdraw = input(f"Are you sure you want to withdraw {withdrawAmount} from the account? Yes/No: ")

                    if verifyWithdraw == 'yes':
                        print('Verified withdraw')
                    else:
                        break

                    if withdrawAmount < accountObj.getBalance():
                        # Calling withdraw method
                        accountObj.withdraw(withdrawAmount)
                        # Printing updated balance
                        print(f"Your updated balance is {accountObj.getBalance()}")
                    else:
                        print(f"Your balance is less than the withdrawal amount you entered {accountObj.getBalance()}\n")
                        print(f"Please make a deposit")

                # Deposit
                elif option == 3:
                    # Reading amount
                    depositAmount = float(input("Enter your amount to deposit: "))
                    verifyDeposit = input(f"Are you sure you want to deposit {depositAmount} into the account? Yes/No: ")

                    if verifyDeposit == 'yes':
                        print("Verified deposit")
                        # Calling deposit method
                        accountObj.deposit(depositAmount)
                        # Printing updated balance
                        print(f"Your updated balance is {accountObj.getBalance()}")
                    else:
                        break

                # Exit
                elif option == 4:
                    print("Transaction is now complete")
                    print(f"Transaction number: {random.randint(10000, 1000000)}")
                    print(f"Current Interest Rate: {accountObj.annualInterestRate}")
                    print(f"Monthly Interest Rate: {accountObj.annualInterestRate / 12}")
                    print(f"Thank you for choosing us as your bank.")
                    exit()
                
                # Any other choice
                else:
                    print("Please enter valid choice!")

# main function
main()
