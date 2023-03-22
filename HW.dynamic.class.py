# dynamic
# world of banks
'''
* ENCAPSULATION - wrapping data and the methods that work on data within one unit.This puts restrictions 
on accessing variables and methods directly and can prevent the accidental modification of data. 

* Getter: A method that allows you to access an attribute in a given class
* Setter: A method that allows you to set or mutate the value of an attribute in a class'''

class Bank:
    #constructor
    def __init__(self, balance = 0):
        self.check_balance_type (balance)
        self.__balance = balance        # private

    def getBalance(self):            
        return self.__balance
    
    def setBalance(self, balance):
        self.check_balance_type (balance)
        self.__balance = balance 
    
# HW1: Type checking method
    def check_balance_type (self, balance):
        if type (balance) != int:
            raise TypeError ("Only integer values accepted")
        
    # to string 
    def __str__(self):
        return f" BANK: {self.__balance}"

class LocalBank(Bank):
      def __init__(self, locality, balance = 0): # overriding - adding the locality
        super().__init__(balance)                # delegation (first operation to do, beacause is delegating to first class)
        self.locality = locality                 # ( second operation beause is local logic)
      
      def __str__(self):
        return f" LOCAL BANK:({self.locality}): {self.getBalance()}"

# HW2: new class < Creditbank with properties - max_credit_amount + credit_percentage(interest)
class CreditBank (Bank):
    def __init__(self, max_credit_amount, credit_percentage, balance = 0 ): 
        super().__init__(balance) 
        self.check_balance_type(max_credit_amount)
        self.__max_credit_amount = max_credit_amount
        self.credit_percentage = credit_percentage
    
    def get_max_credit_amount(self): # access to atribuite from outside the class
        return self.__max_credit_amount
    
    def set_max_credit_amount(self, max_credit_amount):
        self.check_balance_type(max_credit_amount)
        self.__max_credit_amount = max_credit_amount
    
    def monthlyPayment(self):
        return self.__max_credit_amount * self.credit_percentage / 100 / 12

    def __str__(self): # override to print all properties in a formatted string
        return f" Max credit amount: {self.__max_credit_amount}, Interest:{self.credit_percentage}%, Monthly payment: {self.monthlyPayment(): .2f}"

    
##############################
world_bank = Bank (1_000_000_000_000)
agro = LocalBank ("Chisinau", 1_000_000)
credit = CreditBank( 1_000_000, 5)


print(world_bank)
print(agro)
print(credit)

# HW3:  

'''
+-------- main program --------------------------------------------------------+
|                                                                              |
|                                                                              |
|  Bank -------> +--- < class > ------------+                                  |
| ^    ^         |                          |                                  |
| |    |         | .__init__(self.balance=0)| <--- world_bank -- +-- obj ---+  |
| |    |         | .__str__(self)     ^ ^   |                    | __balance|  |
| |    |         | .check_balance_type| |   |                    |    ^     |  |
| |    |         |                    | |   |                    +----|-----+  |
| |    |    <------.getBalance() -----|-|-----------------------------+        |
| |    |    ------>.setBalance()------|-|-----------------------------+        |
| |    |         |                    | |   |                                  |  
| |    |         +--------------------|-|---+                                  |
| |    |                              | |                                      |
| |    |                              | | <- delegation                        |
| |    |                              | -------                                |
| | LocalBank -> +--- < class > ------|-----+ |                                |
| |              |                    |     | |                                |
| |              | .__init__(self.    |     | |<-- world_bank -- +-- obj ---+  |
| |              |      locality, balance=0)| |                  |__balance |  |
| |              | .__str__(self)           | |                  | .locality|  |
| |              +--------------------------+ |                  +----------+  |
| CreditBank ---> +--- < class > -----------+ |                                |
|                |                          | |                                |
|                | .__init__(self.  -----------                                |
|                |  .credit,                | <--- world_bank -- +-- obj ---+  |
|                |  .percentage, balance=0) |                    | .credit   | |
|                | .monthly_payment         |                    | .percentage |  
|                | .__str__(self)           |                    | .montly   | |  
|                |                          |                    |    ^      | |
|                |                          |                    +----|------+ |
|           <------.getcredit() ------------|-------------------------+        |
|           ------>.setcredit()-------------|-------------------------+        |   
|                +--------------------------+                                  |
+------------------------------------------------------------------------------+
'''
