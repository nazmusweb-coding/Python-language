# Write a program that accepts a test score (an integer from 0 to 100) and prints the respective letter grade.

# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# 0–59: F

score = int(input('What was the test score? '))

if 90 <= score <= 100:
  print('A')
elif 80 <= score <= 89:
  print('B')
elif 70 <= score <= 79:
  print('C')
elif 60 <= score <= 69:
  print('D')
elif 0 <= score <= 59:
  print('F')
