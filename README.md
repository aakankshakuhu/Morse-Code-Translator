# Morse Code Translator

This project is a simple Morse Code Translator implemented in Python. It allows you to encode text into Morse code and decode Morse code back into text. The translator supports the English alphabet (A-Z), numbers (0-9), and some punctuation marks.

## Features

- Encode text to Morse code.
- Decode Morse code to text.

## Morse Code Dictionary

The Morse code dictionary used in this project includes:

- Letters: A-Z
- Numbers: 0-9
- Punctuation: `,`, `.`, `?`, `/`, `-`, `(`, `)`

## Usage

### Requirements

- Python 3.x

### Running the Translator

1. Clone the repository or download the script.
2. Run the script using Python:

    ```sh
    python morse_code_translator.py
    ```

3. Follow the prompts to encode or decode messages.

### Example

When you run the script, you will see the following menu:
Your own Morse Code Translator!

Encode
Decode

Choose option `1` to encode text to Morse code or option `2` to decode Morse code to text.

#### Encoding

Input:
Enter text to encode.
HELLO WORLD

Output:

The encoded message: .... . .-.. .-.. --- .-- --- .-. .-.. -..


#### Decoding

Input:

Enter Morse code to decode into text (each code should be separated by a space).
.... . .-.. .-.. --- .-- --- .-. .-.. -..


Output:

The decoded message: HELLO WORLD



## Code Explanation

### MorseCode Class

- `__init__`: Initializes the Morse code dictionary.
- `encode_to_morse(text)`: Encodes the given text to Morse code.
- `decode_from_morse(text)`: Decodes the given Morse code to text.

### Main Script

- Prompts the user to choose between encoding and decoding.
- Accepts user input and calls the appropriate method from the `MorseCode` class.
- Displays the encoded or decoded message.

## Contribution

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements or bug fixes are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

This project is inspired by the classic Morse code system used in telecommunication.


