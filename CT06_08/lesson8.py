print("Hello from lesson 8")


# # Task 5: Math Question Generator

# Create a simple program that generate 2 numbers
# between 1 and 50 that the user must add together.​

# Ask the user to input the answer.​

# The output should be one of the following:​
# - If the answer is correct – output "Correct!"​
# - If the answer is wrong – output "Wrong!​


# generate 2 random numbers
# import random

# # generate 2 random numbers and store into variables
# num1 = random.randint(1, 50) # 25
# num2 = random.randint(1, 50) # 37

# # What is 25 + 37 >> Construct the sentence first
# sentence = "What is " + str(num1) + " + "  + str(num2) + "? "

# # Ask for input
# answer = input(sentence)

# # "31" == 31
# # check if answer is correct...
# if int(answer) == num1 + num2:
#     print("Correct!")
# else:
#     print("Wrong!")

# String formatting / String Concatenation

name = "John" # string
age = 14 # integer

# option 1: use + to join sentences
sentence1 = name + " is " + str(age) + " years old."
print(sentence1)

# option 2: in print(), use the comma
sentence2 = name, "is", age, "years old."
print(sentence2)
# print(name, "is", age, "years old.") # automatically converts to string

# option 3: .format()
sentence3 = "{} is {} years old".format(name, age)
print(sentence3)

#option 4: f-string
sentence4 = f"{name} is {age} years old"
print(sentence4)





# ---------------------------------------------------------------

# ## Task 6: Random Multiplication Quiz

# Create a program that generates a certain number of
# random multiplication questions.​
# 1. Ask the user to input how many questions should be asked.​
# 2. Multiply 2 random numbers between 1 and10 and save the 'answer'.​
# 3. Ask the user to input their answer, 'user_answer'.​
# 4. Check if 'user_answer' is equal to 'answer'.

# The output should be one of the following:​
# - If the answer is correct – output "Correct!" ​
# - If the answer is wrong – output "Wrong!​

# ---------------------------------------------------------------

# ## Task 7: Even or Odd Checker

# Write a program that asks the user to enter a number. The
# program then tells the user whether the number is even
# (True) or odd (False).

# Your program needs to:
# 1. Ask user for an integer input.
# 2. Check if there is any remainder when user input is divided
#    by 2 (using '%').
# 3. Print 'True' if number is even, otherwise print 'False'.

# ---------------------------------------------------------------

# ## Task 8: Multiple Check Program

# Create a program where the user enters 2 numbers. The
# program then checks if the first number is a multiple of
# the second number.

# Your program needs to:
# 1. Get user to input 2 numbers.
# 2. Check if there is any remainder when number #1 is divided
#    by number #2
# 3. Print 'True' if number #1 is a multiple of number #2,
#    otherwise print 'False'.

# ---------------------------------------------------------------

# ## Challenge 1: Multiple Check Program

# Create a console-based quiz game that tests the user on general
# knowledge questions. The game will keep track of the user’s score
# and provide immediate feedback on each question.​

# Hints:​
# - Your input() is always a string, andupper or lower case matters.​
# - i.e. "Hello" != "hello"​
# - Use .lower() or .upper() to change toa same case.​

# ---------------------------------------------------------------

# ## Challenge 2: Guess the Number Game

# Write a Python program that generates a random number between 1 and 100
# and then allows the user to guess what the number is. The program should give
# the user feedback on whether their guess is too high, too low, or correct. The
# user should have a limited number of attempts to guess the number correctly.​

# Advanced features:​

# 1. Allow the user to choose a difficulty level at the beginning of the
# game, which will adjust the range from which the random number
# is generated, or the number of attempts allowed.​

# 2. Implement a scoring system where the user starts with a certain
# score, and points are deducted based on the number of attempts
# taken to guess the number correctly. The fewer attempts used, the
# higher the final score.​

# 3. After a game finishes, whether the user guesses the number or
# runs out of attempt, offer them the option to play again.​

# 4. Provide a hint after a certain number of incorrect guesses, such as
# indicating if the guess is within a certain range of the target
# number (e.g. within 10 numbers higher or lower).​