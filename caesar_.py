import string                # This is a stock Python module.


print()


input_text = str(input("Input text (Don't enter numbers):- "))

print()


shifts = int(input("Input Shift (The shift number should be less than or equal to 26):- "))



alphabet_list = [string.ascii_uppercase, string.ascii_lowercase, string.punctuation]



def caesar(text, shift, alphabets):



    def shifter(alphabet):



        return alphabet[shift::1] + alphabet[:shift:1]



    shift_mapper = tuple(map(shifter, alphabets))


    original_alphabets = ''.join(alphabets)

    shifted_alphabets = ''.join(shift_mapper)



    translation_table = str.maketrans(original_alphabets, shifted_alphabets)



    return text.translate(translation_table)




if __name__ == "__main__":


    # Execute the caesar() function :-

    print()

    print(caesar(input_text, shifts, alphabet_list))                  # print the return value of the caesar() function.





# str.maketrans(og_alphabets, shifted_alphabets) places the two strings one below the other and "maps" each and every character in those strings.



# shifted_text = text.translate(translation_table)
