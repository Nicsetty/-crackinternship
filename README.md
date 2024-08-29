## Caesar Cipher Program

This program implements the Caesar cipher encryption and decryption algorithm. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### Functions

1. **Encryption Function (`caesar_cipher_encrypt`)**
   - **Description:** Encrypts a given text by shifting each alphabetic character by a specified shift value. Non-alphabetic characters are left unchanged.
   - **Parameters:**
     - `text` (str): The message to be encrypted.
     - `shift` (int): The number of positions each letter in the text should be shifted.
   - **Returns:** The encrypted text with each alphabetic character shifted by the given value.

2. **Decryption Function (`caesar_cipher_decrypt`)**
   - **Description:** Decrypts a previously encrypted message by calling the `caesar_cipher_encrypt` function with the negative of the shift value.
   - **Parameters:**
     - `text` (str): The encrypted message to be decrypted.
     - `shift` (int): The number of positions each letter was shifted during encryption.
   - **Returns:** The decrypted text, which is the original message before encryption.

3. **Main Function (`main`)**
   - **Description:** Prompts the user to choose between encryption and decryption. It then requests the message and shift value from the user. Based on the user’s choice, it either encrypts or decrypts the message and displays the result.
   - **Usage:**
     - Run the program and select whether you want to encrypt or decrypt a message.
     - Enter the message and the shift value as prompted.
     - The program will display the encrypted or decrypted message accordingly.

### Example

To encrypt a message:
```plaintext
Select encryption.
Enter the message: Hello World!
Enter the shift value: 3
The output will be: Khoor Zruog!
