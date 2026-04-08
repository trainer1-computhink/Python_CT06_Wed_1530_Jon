# =========================================
# ANSWER SHEET
# =========================================

# ==============================
# SET A — while <condition>:
# ==============================

# A1
num = 2
while num <= 20 and num != 14:
    print(num)
    num += 3

# A2
count = 30
while count >= 10 and count != 18:
    print(count)
    count -= 4

# A3
x = 1
total = 0
while x <= 8 and x != 5:
    total += x
    x += 1
print(total)

# A4
n = 24
while n > 0 and n != 9 and n != 15:
    print(n)
    n -= 3

# A5
a = 3
b = 1
while a < 20 and b < 6:
    print(a * b)
    a += 4
    b += 1


# ==============================
# SET B — while condition + break
# ==============================

# B1
num = 1
while num <= 20:
    if num % 4 == 0 or num % 7 == 0:
        print("STOP")
        break
    print(num)
    num += 3

# B2
total = 0
n = 2
while total < 50:
    total += n
    if total == 20 or total == 35:
        print("Break at", total)
        break
    print(total)
    n += 3

# B3
num = int(input("Enter number: "))
while num != 99:
    if num < 0 or num > 50:
        print("Invalid")
        break
    print("Try again")
    num = int(input("Enter number: "))

# B4
numbers = [5, 9, 12, 15, 18, 21]
i = 0
while i < len(numbers):
    if numbers[i] % 4 == 0 or numbers[i] % 7 == 0:
        print("Found special number")
        break
    print(numbers[i])
    i += 1

# B5
x = 50
while x >= 0:
    if x < 10 or x == 26:
        print("Emergency stop")
        break
    print(x)
    x -= 8


# ==============================
# SET C — while True + break
# ==============================

# C1
while True:
    password = input("Enter password: ")
    if password == "dragon" or password == "tiger":
        break
    if len(password) <= 1:
        print("Too short")
    else:
        print("Wrong password")

# C2
while True:
    num = int(input("Enter number: "))
    if num > 0 and num % 3 == 0 and num % 2 != 0:
        break
    print("Not correct yet")

# C3
while True:
    cmd = input("Enter command: ")
    if cmd == "exit" or cmd == "quit":
        break
    if cmd != "start" and cmd != "help" and cmd != "exit" and cmd != "quit":
        print("Unknown command")
    else:
        print("Accepted command")

# C4
while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a > b and (a - b) < 5:
        break
    if a == b or a < b:
        print("Order not correct")
    else:
        print("Difference too big")

# C5
while True:
    word = input("Enter word: ")
    if word.startswith("s") and word.endswith("p") and word != "stop":
        break
    if word == "stop" or word == "skip":
        print("Blocked word")
    else:
        print("Try another word")
