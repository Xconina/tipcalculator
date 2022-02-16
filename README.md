# tipcalculator
Analysis
	I need a program to compute a tip on a total monetary amount.

Analysis for Tip Calculator- Ashley Cook

Specs
	Input: Total monetary amount in dollars and cents - named totalAmount
		   Tip as a percent - named percentage
    Output:Tip in monetary format - named tipAmount
    Correlation: tipAmount = (percentage * 0.01) * totalAmount

Design
	Print description of program
	Prompt for input, totalAmount
	Prompt for input, percentage
	Expression to correlate inputs and outputs
	Print "The amount of the tip is" tip amount

Code

	#tipcalculator.py
	#This program calculates the tip of a monetary amount
	#by Ashley Cook

	def main():
		print("This program calculates the tip of a total monetary amount")
		totalAmount = input("Enter a total monetary amount in dollars and cents")
		percentage = input("Enter the tip in a percentage")
		tipAmount = (percentage * 0.01) * totalAmount
		print ("THe amount of the tip is", tipAmount)

		main ()

Debugging
	The line tipAmount = ... produces: TypeError: can't multiply sequence by non-int of type 'float'

	After trying many different things and messing with the code, I get it to work by specifying float for each input

Final Code
	#tipCalculator.py
	#This program calculates the tip of a monetary amount
	#by Ashley Cook


                         
	def main():
    	print ("This program calculates the tip of a monetary amount.")
    	totalAmount =float(input("Enter a total monetery amount in dollars and cents(ex. 12.50, 21.75):"))
    	percentage = float(input("Enter the tip as a percentage (ex. 15.0, 22):"))
    	tipAmount= (percentage * 0.01) * totalAmount
    	print ("The amount of the tip is", tipAmount)


	main()

    
