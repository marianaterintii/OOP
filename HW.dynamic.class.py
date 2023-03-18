# dynamic
# world of banks

class Bank:
    #constructor
    def __init__(self, balance = 0):
        self.check_balance_type (balance)
        self.__balance = balance        # private

    def getBalance(self):               # method get/set for acces into private properties
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
    def __init__(self, max_credit_amount, balance = 0 ): 
        super().__init__(balance) 
        self.max_credit_amount, = max_credit_amount,
        if type (max_credit_amount,) != int:
            raise TypeError ("Only integer values accepted") 

    def __str__(self):
        return f" Max credit amount: {self.max_credit_amount}, Interest:{self.getBalance()}"

    
##############################
world_bank = Bank (1_000_000_000_000)
agro = LocalBank ("Chisinau", 1_000_000)
credit = CreditBank( 1_000_000, 5000)


print(world_bank)
print(agro)
print(credit)

# HW3:  - in proces

'''
+-------- main program --------------------------------------------------------+
|                                                                              |
|                                                                              |
|  Bank -------> +--- < class > ------------+                                  |
| ^    ^         |                          |                                  |
| |    |         | .__init__(self.balance=0)| <--- world_bank -- +-- obj ---+  |
| |    |         | .__str__(self)     ^     |                    | __balance|  |
| |    |         | .check_balance_type|     |                    |    ^     |  |
| |    |         |                    |     |                    +----|-----+  |
| |    |    <------.getBalance() -----|-------------------------------+        |
| |    |    ------>.setBalance()------|-------------------------------+        |
| |    |         |                    |     |                                  |  
| |    |         +--------------------|-----+                                  |
| |    |                              |                                        |
| |    |                              |<-delegation                            |
| |    |                              |                                        |
| | LocalBank -> +--- < class > ------|-----+                                  |
| |              |                    |     |                                  |
| |              | .__init__(self.    |     | <--- world_bank -- +-- obj ---+  |
| |              |      locality, balance=0)|                    |__balance |  |
| |              | .__str__(self)           |                    | .locality|  |
| |              +--------------------------+                    +----------+  |
| CreditBank ---> +--- < class > -----------+                                  |
|                |                          |                                  |
|                | .__init__(self.          | <--- world_bank -- +-- obj ---+  |
|                |  .credit, balance=0)     |                    | .balance |  |
|                | .__str__(self)           |                    | .credit  |  |
|                +--------------------------+                    +----------+  |
+------------------------------------------------------------------------------+
'''