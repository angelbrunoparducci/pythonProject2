#Parent class
class User() :
    def __init__ (self, first_name: object, last_name: object, tittle: object, preferred_pronouns: object, date_of_birth: object, occupation: object,
                  account_balance: object,
                  overdraft_limit: object)  -> object:
     self.first_name = first_name
     self.last_name = last_name
     self.tittle = tittle
     self.preferred_pronouns = preferred_pronouns
     self.date_of_birth = date_of_birth
     self.occupation = occupation
     self.account_balance = account_balance
     self.overdraft_limit = overdraft_limit

    def show_client_details (self):
     print('Client Details')
     print('')
     print('First name' , self.first_name)
     print('Last name', self.last_name)
     print('Tittle', self.tittle)
     print('Preferred pronouns', self.preferred_pronouns)
     print('Date of birth', self.date_of_birth)
     print('Occupation', self.occupation)
     print('Account balance', self.account_balance)
     print('Overdraft limit', self.overdraft_limit)

# Child class
class Bank (User):
   def __init__ (self, first_name, last_name, tittle, preferred_pronouns, date_of_birth, occupation, account_balance,
              overdraft_limit):
    super(). __init__ (first_name, last_name, tittle, preferred_pronouns, date_of_birth, occupation, account_balance, overdraft_limit):
    self.balance = 0

   def deposit (self. amount):
    self.amount = amount
    self.balance = self.balance + self.amount

   def withdraw (self. amount):
    self.amount = amount
    if self.amount > self.balance:
     print ('Not enough funds | Funds Available: £', self.balance )

