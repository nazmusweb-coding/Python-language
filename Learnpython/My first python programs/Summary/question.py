# Question in photo

initial_amount = float(input('What is the initial amount? '))
interest_rate = float(input('What is the annual interest rate as a percent? '))
compounding_frequency = float(input('How many times in a year is the amount compounded? '))
time = float(input('How many years are you going to wait? '))

final_amount = initial_amount*((1+(interest_rate/(100*compounding_frequency)))**(compounding_frequency*time))

print('At the end of the period, you will have', final_amount)