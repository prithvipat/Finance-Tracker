from user import User

print("""
    ---------------------------------  
    Welcome to Your Finacial Tracker!
    ---------------------------------
            Prithvi Paturi          |
    ---------------------------------
      1) Checking Bank Details
      2) Create expense
      3) insert money into account
    """)

account = User(120000, 100, 10000, 1000)

account.transaction(10, "Tims")
print("")
account.getDetails()
print("")
account.getTransactions()
account.transaction(12, "Starbucks")

account.getTransactions()


"""
salary = int(input("Enter Your Salary"))
credit_score = int(input("Enter Your Credit Score"))

account = User(salary, credit_score)

while True:
    user = int(input(""))

    if user == 1:
        account.getDetails()

    elif user == 2:
        break
"""