import string
import random
while True:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    part_letters = random.choices(letters, k=random.randint(8, 63))
    part_digits  = random.choices(digits, k=random.randint(8, 63))
    part_symbols = random.choices(symbols, k=random.randint(8, 63))
    full_list = part_letters + part_digits + part_symbols
    random.shuffle(full_list)
    final_password = "".join(full_list)
    input(final_password)
    continue