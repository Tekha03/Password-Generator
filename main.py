import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'g', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
user_num_letters = int(input("How many letters would you like in your password?\n"))
user_num_numbers = int(input("How many numbers would you like?\n"))
user_num_symbols = int(input("How many symbols would you like?\n"))

password_list = []
for i in range(0, user_num_letters):
    password_list += random.choice(letters)
for i in range(0, user_num_numbers):
    password_list += random.choice(numbers)
for i in range(0, user_num_symbols):
    password_list += random.choice(symbols)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")