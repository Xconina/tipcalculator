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

    
