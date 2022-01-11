class atm:
    def _init_(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def check_balance(self):
        print('your balance is 50,000')
    def withdrawl(self, amount):
        new_amount = 50,000-amount
        print('you have withdrawl amount'+str(amount)+''.your remaining balance is'+str(new_amount))

def main():
    card_number = input('insert your card number')
    pin_number = input('enter your pin number')
    new_user = atm(card_number, pin_number)
    print('choose your activity')
    print('1.balance inquiry  2. withdrawl')
    activity = int(input('enter activity number'))

    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input('enter the amount'))
        new_user.withdrawl(amount)
    else:
        print('enter a valid number')
if _name_=='_main_':