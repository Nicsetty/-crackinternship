How the program works?
1.Encryption Function (caesar_cipher_encrypt):
This function takes a text and a shift value.
It iterates over each character in the text, and if it's an alphabetic character, it shifts it by the given shift value while keeping the case (uppercase or lowercase) the same.
Non-alphabet characters are left unchanged.
The result is the encrypted text.

2.Decryption Function (caesar_cipher_decrypt):
This function calls the caesar_cipher_encrypt function with the negative of the shift value to reverse the encryption process.

3.Main Function (main):
The user is prompted to choose whether they want to encrypt or decrypt a message.
The program then asks for the message and the shift value.
Based on the user's choice, it either encrypts or decrypts the message and displays the result.
