class Atm:
    def __init__(self, pin, balance) -> None:
        self._pin = pin  # Making the PIN private
        self._balance = balance  # Making the balance private
        self._attempts_left = 3  # Adding attempts_left property for PIN attempts
        #self.menu()

    def _validate_pin(self, entered_pin):
        if entered_pin == self._pin:
            return True
        else:
            print(f"Invalid PIN. Attempts left: {self._attempts_left}")
            self._attempts_left -= 1
            return False

    def check_balance(self):
        print("Checking balance ...")
        print(f'Current balance: ${self._balance}')

    def deposit(self):
        print("Proceed for depositing money")
        try:
            money = input("Enter the amount: $")
            money = int(money)
            if money > 0:
                self._balance += money
                print(f'The new balance is ${self._balance}')
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        print("Proceed for withdrawing money")
        entered_pin = input("Enter the PIN: ")
        if self._validate_pin(entered_pin):
            try:
                money = input("Enter the amount: $")
                money = int(money)
                if money > 0:
                    remain = self._balance - money
                    if remain >= 0:
                        self._balance = remain
                        print("Withdrawal successful")
                        print(f'The new balance is ${self._balance}')
                    else:
                        print("Can't withdraw more than balance")
                else:
                    print("Invalid amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            if self._attempts_left == 0:
                print("Too many unsuccessful attempts. Exiting...")
                exit()
    
    def change_pin(self):
        print("Proceed for changing Pin")
        entered_pin = input("Enter the PIN: ")
        if self._validate_pin(entered_pin):
            self._pin=entered_pin
            print("PIN change successfully")
        else:
            print("Invalid pin. Please enter a valid number.")

    def menu(self):
        while True:
            user_input = input("""How would you like to proceed? 
                             1. Enter 1 for check balance
                             2. Enter 2 for withdraw
                             3. Enter 3 for deposit
                             4. Enter 4 for change pin
                             5. Enter 5 for Exit 
                             """)

            try:
                user_input = int(user_input)
                if user_input == 1:
                    self.check_balance()
                elif user_input == 2:
                    self.withdraw()
                elif user_input == 3:
                    self.deposit()
                elif user_input == 4:
                    self.change_pin()
                elif user_input == 5:
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")




