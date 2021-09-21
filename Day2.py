print("Welcome to the Tip-Calculator")

bill= input("Enter the total bill: ")
bill= float(bill)

people = input("Enter the number of people present: ")
people = int(people)

tax= input("Enter the tax amounted over the bill: ")
tax = float(tax)

total_bill = bill+bill*tax*0.01
total_bill= round(total_bill,people)
print("The total bill after considering the taxes are:"+ format(total_bill,f".{people}f"))

bill_each=total_bill/people
bill_each= "{:.2f}".format(bill_each)
print(f"\nBill to be paid by {people} people after considering the taxes is : {bill_each} each")
