# encryption.py
# Hareem Khan, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.


print("ENDG 233 Encryption Program")

### Define your functions here

import string

def variable_function():
    """ variable function houses all user inputs and created variables, as well as the validation of the inputted cypher by the user.
     No arguments required in this function.
     no return required for this function
    
    """

    while True:                                                                                             # continuous user input loop here, which means that unless 0 is entered by the user, the user will be continuously prompted to use the encryption program.
        user_choice = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')           # user choice prompts the user to decide whether they want to encode text, decode text, or quit the program.
        if user_choice == '0':                                                                              # if the user selects '0' for user choice, the cose will break and print the closing statement.
            break

        processed_text = input('Please enter the text to be processed: ')                                   # processed_text is an inputted string that represents the message that the user wants to be encoded or decoded.
        user_cypher = input('Please enter the cipher text: ')                                               # user_cipher is an inputted string that represents the cypher the user inputs to encode or decode the message.
        lower_alphabet = string.ascii_lowercase                                                             # lower case ascii alphabet is used with the inputted cypher in the encode and decode functions.

        alphabet_list = list(lower_alphabet)                                                                # a list of the lowercase alphabet is created to later make a dictionary with the cypher list.
        cypher_list = list(user_cypher)                                                                     # a list of the user_cypher is created to later make a dictionary with the alphabet list.

        
        if user_choice == '1':                                                                              # if the user inputs '1' into the code, the encoding function will be called if their cypher is valid, and their message will be encoded. 
            encode_1 = encode_function(alphabet_list, processed_text, cypher_list)
            if len(user_cypher) == 26:                                                                      # if the user_cypher is made up of 26 unique elements, it is valid and the user will be notified of its validity. 
                if len(set(user_cypher)) == len(user_cypher):
                    print('Your cipher is valid.')
                    print('Your output is:', encode_1)                                                      # after varifying the cypher, the encode function is called, and then the encoded text is printed to the output for the user. 
                else:
                    print('Your cipher is invalid, it must contain 26 unique elements of a-b or 0-9.')      # if the user_cypher is not made up of 26 unique elements, it is invalid and the user will be notified of this, then prompted to start again with the program. 
            else:
                print('Your cipher is invalid, it must contain 26 unique elements of a-b or 0-9.')
            

        if user_choice == '2':                                                                              # if the user inputs '2' into the code, the decoding function will be called if their cypher is valid, and their message will be decoded.
            decode_2 = decode_function(alphabet_list, processed_text, cypher_list)
            if len(user_cypher) == 26:                                                                      # if the user_cypher is made up of 26 unique elements, it is valid and the user will be notified of its validity.
                if len(set(user_cypher)) == len(user_cypher):
                    print('Your cipher is valid.')
                    print('Your output is:', decode_2)                                                      # after varifying the cypher, the decode function is called, and then the decoded text is printed to the output for the user.
                else:
                    print('Your cipher is invalid, it must contain 26 unique elements of a-b or 0-9.')      # if the user_cypher is not made up of 26 unique elements, it is invalid and the user will be notified of this, then prompted to start again with the program.
            else:
                print('Your cipher is invalid, it must contain 26 unique elements of a-b or 0-9.')



def encode_function(alphabet_list, processed_text, cypher_list):                                            
    """ The encode function is called when '1' is inputted into the code, and then the inputted message will be encoded with the valid cypher.
    Parameters
    alphabet_list: a list representing the lowercase alphabet
    processed_text: a string that represents the inputted message from the user that will be encoded here
    cypher_list: a list representing the inputted cypher by the user
    Return
    This function returns encode_text, which is the encoded message that is sent to the output

    """

    dictionary_1 = dict(zip(alphabet_list, cypher_list))                                                    # a dictionary is created with the lowercase alphabet, and the user's valid cypher as it's keys, which is used to encode the message.

    encode_text = ""
    for i in processed_text:                                                                                # each element of the inputted message is converted from the lowercase alphabet, to the inputted cypher to create the encoded message.
        encode_text += dictionary_1[i]

        
    return  encode_text                                                                                     # the encoded text is then returned from the function.
    

def decode_function(alphabet_list, processed_text, cypher_list):                                              
    """the decode function is called when '2' is inputtted into the code, and then the inputted encode message will be decoded with the valid cypher.
    Parameters
    alphabet_list: a list representing the lowercase alphabet
    processed_text: a string that represents the inputted message that will be decoded here
    cypher_list: a list representing the inputted cypher by the user
    Return
    This function returns decode_text, which is the decoded message that is sent to the output

    """

    dictionary_2 = dict(zip(cypher_list, alphabet_list))                                                    # a dictionary is created with the user's valid cypher, and the lowercase alphabet as it's keys, which is used to decode the message.

    decode_text = ""
    for i in processed_text:                                                                                # each element of the inputted encode message is converted from the user's cypher, back to the lowercase alphabet to create the decoded message. 
        decode_text += dictionary_2[i]
 

    return decode_text                                                                                      # the decoded text is then returned from the function. 
 
    
variable_function()                                                                                         # the variable function is called, which begins the program
      

print('Thank you for using the encryption program.')                                                        # Closing statement prints when '0' is inputted by user. 

