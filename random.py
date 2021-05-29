import random

import string

#Random Password Generator

lower = string.ascii_lowercase

upper = string.ascii_uppercase

s = ""

for i in range(0, 9):

    s = s + str(i);

symbols = """"`-=\~!@#$%^&*()_+|[]{};':",.<>/?"""

all = lower + upper + str(s) + symbols

len = input('\U0001F536 '+'Enter the length '+'\U0001F536 ')

count = int(input('\U0001F537 '+'Number of Passwords Required '+'\U0001F537 '))

print('\U0001F4A0 '+'Combinations Available'+' \U0001F4A0')

for count in range(0, count):

    password = "".join(random.sample(all, int(len)))

    print('\U0001f441',password)
