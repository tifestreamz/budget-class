class budget:
    def __init__(self, amount):
        self.amount = amount

    def deposit(self):
        deposit_amount = int(input("How much do you want to deposit?  \n"))
        self.amount = deposit_amount
        print("you've deposited %d into this category" %self.amount)

    def withdraw(self):
        withdrawal_amount = int(input("How much do you want to deposit?  \n"))
        self.amount = withdrawal_amount
        print("you've deposited %d into this category" %self.amount)

    # Transferring balance amounts between categories

    def balanceTransfer(self):
        pass
    
food = budget(20000)
food.deposit()
food.withdraw()

transportation = budget(30000)
transportation.deposit()
transportation.withdraw()


