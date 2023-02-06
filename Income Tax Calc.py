
print("Hello! This program will allow you to calculate your income tax!")

Income1 = float(input("Enter the gross income: "   ))

Income = round(Income1, 2)

Dependent1 = float(input("Enter the number of dependents: "))

Dependent = round(Dependent1, 0)

Tax1 = round((Income - 10000 - (Dependent*3000)), 2)

Tax = round((Tax1*0.2), 2)

print("The income tax is:  $", Tax)

Income2 = round((Income - Tax), 2)

print("The Income after Tax is:  $", Income2)


