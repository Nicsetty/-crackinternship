import tkinter as tk
from tkinter import messagebox

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

def on_encrypt():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        encrypted_message = caesar_cipher_encrypt(message, shift)
        result_label.config(text=f"Encrypted Message: {encrypted_message}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")

def on_decrypt():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        decrypted_message = caesar_cipher_decrypt(message, shift)
        result_label.config(text=f"Decrypted Message: {decrypted_message}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")

# Creating the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Creating and placing widgets
tk.Label(root, text="Enter your message:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Enter the shift value (an integer):").pack(pady=5)
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack(side=tk.LEFT, padx=20, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.pack(side=tk.RIGHT, padx=20, pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Running the application
root.mainloop()
