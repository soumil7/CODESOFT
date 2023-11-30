import random
import array

try:
    MAX_LEN = int(input("Enter the desired password length: "))
except ValueError:
    print("Please enter a valid number.")

# Define character sets
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

combined_list = digits + uppercase_characters + lowercase_characters + symbols

rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase_characters)
rand_lower = random.choice(lowercase_characters)
rand_symbol = random.choice(symbols)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


for _ in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(combined_list)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for char in temp_pass_list:
    password = password + char

print(password)
