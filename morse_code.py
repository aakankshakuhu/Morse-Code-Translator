class MorseCode:
    def __init__(self, ):
        self.morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
        }

    def decode_from_morse(self, text):
        text += " "
        key_list = list(self.morse_code_dict.keys())
        val_list = list(self.morse_code_dict.values())
        received_message = ""
        morse_letter = ""
        for code in text:
            if (code!=" "):
                morse_letter += code
            else:
                if morse_letter in val_list:
                    position = val_list.index(morse_letter)
                    key_to_be_found = key_list[position]
                    received_message += key_to_be_found
                    morse_letter = ""
                else:
                    received_message += " "
        return received_message


    def encode_to_morse(self, text):
        received_message = " "
        for code in text:
            if(code!=' '):
                letter = self.morse_code_dict.get(code)
                received_message += letter
            else:
                received_message += "   "
        return received_message.strip()


translator = MorseCode()
print("Your own Morse Code Translator!")
print("1. Encode")
print("2. Decode")

choice = int(input("Choose from options 1 or 2. \n"))

if(choice==1):
    text = input("Enter text to encode. \n")
    encoded = translator.encode_to_morse(text.upper())
    print("The encoded message: ", encoded)

elif(choice==2):
    text = input("Enter morse code to decode into text (each code should be separated by a space). \n")
    decoded = translator.decode_from_morse(text)
    print("The decoded message: ", decoded)
else:
    print("Please choose a valid option.")
