 #Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(Self):
        Self.balance=0
        print('Hello!!! Welcome to the Deposit & Withdrawal Machine')
 
    def __deposit__(Self):
        Amount=float(input('Enter amount to be Deposited: '))
        Self.balance += Amount
        print('\n Amount Deposited:',Amount)
 
    def __withdraw__(Self):
        Amount = float(input('Enter amount to be Withdrawn: '))
        if Self.balance>=Amount:
            Self.balance-=Amount
            print('\n You Withdrew:', Amount)
        else:
            print('\n Insufficient balance  ')
 
    def __display__(Self):
        print('\n Net Available Balance=',Self.balance)
 
# Driver code
  
# creating an object of class
S = Bank_Account()
  
# Calling functions with that class object
S.__deposit__()
S.__withdraw__()
S.__display__()