# Convert between types

#Luckily, we can use functions that convert between data types:

# str(x) converts x into a string,
# int(x) converts x into an integer,
# float(x) converts x into a floating point number.


rate = input('What is your hourly rate?')
w_hr = input('How many hours have you worked?')
income = float(rate) * float(w_hr)
print('You have earned', income, 'in total!')


# perfect! input() is a very convenient function, but there is one catch: user input is always treated as a string value, even if a number is provided. If you ask for a number with input() and then try to add it to another number, Python will throw an error.