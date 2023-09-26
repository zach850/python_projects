#If the bill was $150.00, split between 5 people, with 12% tip. 


#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator! ")
total_bill = input("What is the total bill? ")
tip = input("What size tip do you want to leave? ")
amount_ppl = input("Spilt between how many people? ")

total_payment = (float(total_bill) / int(amount_ppl)) * (int(tip) / 100) 
print(f"Your total bill per person is {round(total_payment, 2)}")