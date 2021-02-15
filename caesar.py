import string



alphabets_lower = string.ascii_lowercase


alphabets_upper = string.ascii_uppercase



plain_text = "hkpafh uhtiphy"


shift = len(alphabets_lower) - 7        # len(alphabets_lower) == 26

shift = shift % len(alphabets_lower)




alphabets_lower_shifted = alphabets_lower[shift::1] + alphabets_lower[:shift:1]


# Now, let's create a "translation table".

translation_table = str.maketrans(alphabets_lower, alphabets_lower_shifted)



# What str.maketrans() function does that it places the two passed in string objects one below the other and then maps each of the individual characters.


encrypted_text = plain_text.translate(translation_table)

print()

print(encrypted_text)










# alphabet_set "ABCDEFG"

# alphabet_set_shift_two = "CDEFGAB"
