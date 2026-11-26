class BankAccount:
    def __init__(self):
        self.balance = 750
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient founds. Check your balance.")
        else:
            self.balance -= amount
    
    def show_balance(self):
        print(f"Your current balance is ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.min_balance = 500
    
    def withdrawal(self, amount):
        try:
            if (self.balance - amount) < self.min_balance:
                raise ValueError("Insufficient founds. You have to keep a minimum balance.")
            else:
                self.balance -= amount
        except ValueError as err:
            print(err)

def type_menu():
    normal_account = BankAccount()
    savings_account = SavingsAccount()
    flag = True
    while flag:
        print("----ATM MENU----")
        print("1. Normal Account")
        print("2. Savings Account")
        print("E. Exit")
        user_input = input("\nChoose your option: ")
        
        if user_input == '1':
            main_menu(user_input, normal_account)
        
        elif user_input == '2':
            main_menu(user_input, savings_account)
        
        elif user_input == 'E' or user_input == 'e':
            flag = False
            print("Thank you for using MartinZeta Systems.\nHave a nice day!")
        
        else:
            print("Invalid option. Try again.")

def main_menu(account_type, account):
    flag = True
    while flag:
        if account_type == '1':
            print("----NORMAL ACCOUNT MENU----")
        else:
            print("SAVINGS ACCOUNT MENU")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Show balance")
        print("E. Back")
        user_input = input("\nChoose your option: ")
        
        if user_input == '1':
            try:
                deposit_amount = get_valid_amount('Deposit')
                account.deposit(amount=deposit_amount)
                account.show_balance()
            except ValueError as err:
                print("Amount must be a valid number.")
        
        elif user_input == '2':
            try:
                withdrawal_amount = get_valid_amount('Withdrawal')
                account.withdrawal(amount=withdrawal_amount)
                account.show_balance()
            except ValueError as err:
                print("Amount must be a valid number.")
        
        elif user_input == '3':
            account.show_balance()
        
        elif user_input == 'E' or user_input == 'e':
            flag = False
            print("Thank you for using MartinZeta Systems.\nHave a nice day!")
        
        else:
            print("Invalid option. Try again.")

def get_valid_amount(transaction):
    while True:
        try:
            amount = input(f"{transaction} amount: $").strip()
            for i in amount:
                if i.isalpha():
                    raise ValueError("Amount can only contain numbers.")
            if not float(amount):
                raise ValueError("Amount must be a valid number.")
            elif float(amount) < 0:
                raise ValueError("Amount must be greater than zero.")
            elif '.' in amount:
                if len(amount.split('.')[1]) > 2:
                    raise ValueError("Amount can only have two decimals.")
                else:
                    return float(amount)
            else:
                return float(amount)
        except ValueError as err:
            print(err)
        

def main():
    type_menu()

if __name__ == '__main__':
    main()