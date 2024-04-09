# Create a list of names and print the second item

names = ['Sakib', 'Rakib', 'Aakib', 'Hakib', 'Nakib']
print(names[1])

# Create a list of sports and then replace the second item with another sport.

sports = ['Football', 'Cricket', 'Kabadi', 'Badminton']
sports[1] = 'Kana machi bow bow'

# Create a list containing numbers and delete the fifth number from the array.

numbers = [1, 2, 3, 4, 5]
del numbers[4]

# Create two lists of numbers and merge them.

list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2

# Create a list of numbers and find the length, minimum, and maximum

list_numbers = [1, 2, 3, 4, 5, 6, 123, 13, -1, 122]
print(f"Lenght = {len(list_numbers)}, Mininum = {min(list_numbers)}, Maximum = {max(list_numbers)}")

# Create a dictionary of students and scores and print out a student’s score

students = {'Shaka' : 90, 'Kala' : 87, 'Jimbei' : 78, 'Luffy' : -10}
print(students)

# Create a dictionary with the key being names and values being ages and then delete the second key/value pair. 

age_record = {"Shaka" : 100, "Kala" : 200, "Nala" : 300, "Dala" : 400}
del age_record['Kala']

# Create a dictionary of names and ages and then print out all the keys and values

names_and_ages = {"Abul" : 50, "Karim" : 78, "Joshim" : 67, "Kamil" : 60}
print(names_and_ages)

# Create a tuple of your favorite movies

favorite_movies = ("Aashiqui 2", "Salar", "3 idiots", "KGF")

# Create a tuple and print all the items from the first to third index.

favorite_movies = ("Aashiqui 2", "Salar", "3 idiots", "KGF")
print(favorite_movies[0:3])
