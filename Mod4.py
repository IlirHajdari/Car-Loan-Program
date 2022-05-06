val = input("Enter the monthly payment amount: ")
if val == '320':
    print("Great! Your loan options are listed below.")
    print()
    print("Option #1:")
    print("Fix Transmission Loan")
    print("Total amount of loan: $2,500")
    print("Total amount of interest: 17%")
    print("With a monthly payment of", val, "the loan will be paid off in 9 months and will incur an additional $169 during the life of the loan.")
    print()
    print("Option #2:")
    print("Used Car Loan")
    print("Total amount of loan: $9,000")
    print("Total amount of interest: 12%")
    print("With a monthly payment of", val, "the loan will be paid off in 34 months and will incur an additional $1,621 during the life of the loan.")
    print()
    print("Option #3:")
    print("New Car Loan")
    print("Total amount of loan: $20,000")
    print("Total amount of interest: 10%")
    print("With a monthly payment of", val, "the loan will be paid off in 89 months and will incur an additional $8,369 during the life of the loan.")
    print()
else:
    print("That is not correct. The monthly payment should be 320 since that is the amount left at the end of each month.")

def one_two_or_three():
        inp = input("Type in 1 to choose Fix Transmission loan. Type in 2 to choose Used Car loan. Type in 3 to choose New Car loan: ")
        if inp == '1':
            print("Great choice! This option is the most affordable and will cost you the least amount of time and money.")
        elif inp == '2':
            print("This option will cost you more time and money than the first option will.")
        elif inp == '3':
            print("This option will cost you the most time and money than the other two options.")
        else:
            print("You must choose between these three options.")
            return one_two_or_three()
one_two_or_three()
            