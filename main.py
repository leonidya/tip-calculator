#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill?"))
tip = float(input("How much tip would you like to give? 10, 12 of 15"))
people = int(input("how many people splitt the bill?"))
each_person_pay = round((bill/people)*(tip/100+1), 2)
print(each_person_pay)