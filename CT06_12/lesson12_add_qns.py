# =========================================
# SET A — while <condition>:
# Higher difficulty with and / or / not
# =========================================

# A1
# Question:
# Write a program that starts with num = 2.
# Use a while loop to print the value of num while:
# - num is less than or equal to 20
# - AND num is not equal to 14
# Each time, increase num by 3.
#
# Output:
# 2
# 5
# 8
# 11

# A2
# Question:
# Write a program that starts with count = 30.
# Use a while loop to print count while:
# - count is greater than or equal to 10
# - AND count is not 18
# Each time, subtract 4 from count.
#
# Output:
# 30
# 26
# 22

# A3
# Question:
# Write a program that starts with x = 1 and total = 0.
# Use a while loop to add x into total while:
# - x is less than or equal to 8
# - AND x is not 5
# Increase x by 1 each round.
# Print total at the end.
#
# Output:
# 23

# A4
# Question:
# Write a program that starts with n = 24.
# Use a while loop to print n while:
# - n is greater than 0
# - AND n is not 9
# - AND n is not 15
# Each time, subtract 3 from n.
#
# Output:
# 24
# 21
# 18

# A5
# Question:
# Write a program that starts with a = 3 and b = 1.
# Use a while loop while:
# - a is less than 20
# - AND b is less than 6
# In each round:
# - print a * b
# - increase a by 4
# - increase b by 1
#
# Output:
# 3
# 14
# 33
# 60
# 95


# =========================================
# SET B — Bridge (while condition → break)
# Must use while condition and break
# =========================================

# B1
# Question:
# Write a program that starts with num = 1.
# Use a while loop with the condition num <= 20.
# In each round:
# - if num is divisible by 4 OR divisible by 7, print "STOP" and break
# - otherwise print num
# - then increase num by 3
#
# Output:
# 1
# STOP

# B2
# Question:
# Write a program that starts with total = 0 and n = 2.
# Use a while loop with the condition total < 50.
# In each round:
# - add n to total
# - if total is 20 OR total is 35, print "Break at", followed by total, and break
# - otherwise print total
# - then increase n by 3
#
# Output:
# 2
# 7
# 15
# Break at 26

# B3
# Question:
# Write a program that asks the user to enter a number.
# Keep looping while the number is not 99.
# Inside the loop:
# - if the number is less than 0 OR greater than 50, print "Invalid" and break
# - otherwise print "Try again" and ask again
#
# Output:
# If user types:
# 10
# 20
# 60
#
# Output should be:
# Try again
# Try again
# Invalid

# B4
# Question:
# Write a program that checks the list:
# [5, 9, 12, 15, 18, 21]
# using a while loop and an index.
# Keep looping while the index is still inside the list.
# Inside the loop:
# - if the current number is divisible by 4 OR divisible by 7, print "Found special number" and break
# - otherwise print the number
# - move to the next index
#
# Output:
# 5
# 9
# Found special number

# B5
# Question:
# Write a program that starts with x = 50.
# Use a while loop with the condition x >= 0.
# In each round:
# - if x is less than 10 OR x is equal to 26, print "Emergency stop" and break
# - otherwise print x
# - subtract 8 from x
#
# Output:
# 50
# 42
# 34
# Emergency stop


# =========================================
# SET C — while True + break
# Higher difficulty with and / or / not
# =========================================

# C1
# Question:
# Write a program that keeps asking the user to enter a password.
# Use while True.
# Break only when the password is:
# - "dragon"
# - OR "tiger"
# If the password is empty OR only one character long, print "Too short".
# Otherwise print "Wrong password".
#
# Output:
# Example inputs:
# a
# hello
# tiger
#
# Output:
# Too short
# Wrong password

# C2
# Question:
# Write a program that keeps asking the user to enter a number.
# Use while True.
# Break only when the number is:
# - greater than 0
# - AND divisible by 3
# - AND not divisible by 2
# Otherwise print "Not correct yet".
#
# Output:
# Example inputs:
# 4
# 12
# 9
#
# Output:
# Not correct yet
# Not correct yet

# C3
# Question:
# Write a program that keeps asking the user to type a command.
# Use while True.
# Break only if the command is "exit" OR "quit".
# If the command is not "start" AND not "help" AND not "exit" AND not "quit",
# print "Unknown command".
# Otherwise print "Accepted command".
#
# Output:
# Example inputs:
# play
# help
# quit
#
# Output:
# Unknown command
# Accepted command

# C4
# Question:
# Write a program that keeps asking the user to enter two numbers: a and b.
# Use while True.
# Break only when:
# - a is greater than b
# - AND a - b is less than 5
# If a is equal to b OR a is less than b, print "Order not correct".
# Otherwise print "Difference too big".
#
# Output:
# Example inputs:
# a = 3, b = 7
# a = 12, b = 2
# a = 9, b = 6
#
# Output:
# Order not correct
# Difference too big

# C5
# Question:
# Write a program that keeps asking the user to enter a word.
# Use while True.
# Break only when:
# - the word starts with "s"
# - AND ends with "p"
# - AND is not "stop"
# If the word is "stop" OR "skip", print "Blocked word".
# Otherwise print "Try another word".
#
# Output:
# Example inputs:
# stop
# ship
#
# Output:
# Blocked word
