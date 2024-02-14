import datetime

class User:

    def __init__(self, salary, checkings, savings, debt):
        self.salary = salary
        self.checkings = checkings
        self.savings = savings
        self.expenses = []
        self.debt = debt

    def getDetails(self):     # Get detials, 
        print(f"""
    
            Salary:        {self.salary}
            Checkings:     {self.checkings}
            Savings:       {self.savings}
            Debt:          -{self.debt}
              """)
        return 0
    
    def payMortgage(self):
        return 0
    
    def transaction(self, price, item): 
        if self.checkings < price:
            print("Your account doesn't have enough for this transaction, this must be a mistake")

        else:
            self.checkings -= price
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day

            category_mapping = {
                1: "Food",
                2: "Travel",
                3: "Utilities",
                4: "Others"
            }

            print("What did you get: \n 1) Food \n 2) Travel \n 3) Utilities 4) Others")

            lis = [f"{year}:{month}:{day} : {item}: {price}"]


                

    # Setters
    def setSalary(self, newSalary):
        self.salary = newSalary
    
    def setCredit(self, credit):
        self.credit = credit
    
    def setCheckings(self, amount):
        self.checkings = amount
    
    def setDebt(self, debt):
        self.debt = debt
    
    def getTransactions(self):
        print("")
        print(self.dict)

    
    



