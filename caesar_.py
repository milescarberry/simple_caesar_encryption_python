import string                # This is a stock Python module.





input_text = "My name is Aditya Kumar!"


shifts = 10

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
