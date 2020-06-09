#Future Value Calculator
#Nathan Wagstaff
#1/31/2020

#User can input any investment and calculate the value over a set number of years.

#intro
print("Enter in the information as prompted")

#Variable input

investmentAmount = input("Investment Amount: $" )
paymentAmount = input("Monthly Payment: $" )
monthlyInterestRate = input("Annual Interest: ")
numberOfYears = input("Number of Years: ")

#translation to months
numberOfYears = int(numberOfYears)


#translation to int
investmentAmount = int(investmentAmount)
paymentAmount = int(paymentAmount)
monthlyInterestRate = int(monthlyInterestRate)

#conversions
months = numberOfYears * 12
decimalInterest = monthlyInterestRate / 100 / 12

#formula
part1 = investmentAmount * ((1 + decimalInterest)**months)
part2 = paymentAmount * ((((1 + decimalInterest)**months) - 1) / decimalInterest) * (1 + decimalInterest)
futureValue = part1 + part2

#results
print(futureValue)



