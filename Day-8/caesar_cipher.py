alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# encoding




def encrypt(text , shift):
    encode_list =[]
    for i in text:
     current_pos = alphabet.index(i)
     new_pos = (current_pos + shift)%len(alphabet) 
     new_alphabet =  alphabet[new_pos]    
     encode_list.append(new_alphabet) 
    converted_list =''.join(encode_list)    
    print("the encrypted text is " ,converted_list )       






# decoding

def decode(text , shift):
    decoded_list=[]
    for i in text:
     current_pos = alphabet.index(i)
     new_pos = (current_pos - shift)%len(alphabet) 
     new_alphabet =  alphabet[new_pos]    
     decoded_list.append(new_alphabet) 
    converted_list =''.join(decoded_list)    
    print("the decrypted text is " ,converted_list )       



try:
    
    while True:
 
        if   direction == 'encode':
                encrypt(text,shift)
                
        elif direction  == 'decode':
            decode(text,shift)
        elif direction == 'exit':
            print("The program will terminate now")
            break  
    
except ValueError:
    
    print("invalid input")
        
    
    
    

    





    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message

