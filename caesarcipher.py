def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            char_code = ord(char)
            
            if char.isupper():
                base = ord('A')
                encrypted_char = chr((char_code - base + shift_amount) % 26 + base)
            else:
                base = ord('a')
                encrypted_char = chr((char_code - base + shift_amount) % 26 + base)
        else:
            encrypted_char = char  # Non-alphabet characters remain unchanged

        encrypted_text += encrypted_char
    
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
        return

    message = input("Enter your message: ").strip()
    try:
        shift = int(input("Enter the shift value (an integer): ").strip())
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
