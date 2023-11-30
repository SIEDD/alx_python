# import random

# number = random.randint(-10, 10)

# print(number)

# if number > 0:
#      print("is positive")
# elif number == 0:
#      print("is zero")
# elif number < 0:
#      print("is negative")

import random

number = random.randint(-100, 100)

print(f"{number}\n{'is positive' if number > 0 else ('is zero' if number == 0 else 'is negative')}")







