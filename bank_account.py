class Bank_Account:
    def account(self):
        print("Welcome to the Bank Account System")
        self.bankpin=int(input("Bank PIN: "))
        if self.bankpin==1234:
            print("Please choose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Exit")
            choice=int(input("Enter your choice: "))
            if choice==1:
                self.deposit()
                continu=input("Do you want to Continue(yes/no): ")
                if continu.lower()=="yes":
                    self.account()
                else:
                    print("Thank you for using the Bank Account System")
                    exit()
            elif choice==2:
                self.withdraw()
                continu=input("Do you want to Continue(yes/no): ")
                if continu.lower()=="yes":
                    self.account()
                else:
                    print("Thank you for using the Bank Account System")
                    exit()
            elif choice==3:
                self.display_balance()
                continu=input("Do you want to Continue(yes/no): ")
                if continu.lower()=="yes":
                    self.account()
                else:
                    print("Thank you for using the Bank Account System")
                    exit()
            elif choice == 4:
                print("Thank you for using the Bank Account System")
                exit()
            
            else:
                print("Invalid choice")
                self.account()
        else:
            print("Invalid PIN")
            self.account()
    def __init__(self):
        self.balance=0
        print("Wellcome to Deposit & Withdrawal Machine")
    def deposit(self):
        amount=float(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Deposit Successful")
        print(f"Your current balance is: {self.balance}")
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw: "))
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawal Successful")
            print(f"Your current balance is: {self.balance}")
    def display_balance(self):
        print(f"Your current balance is: {self.balance}")      
          
s = Bank_Account()
s.account()