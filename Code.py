# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97  # Base for uppercase or lowercase letters
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

# Function to decrypt the encrypted text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)  # Uses the same algorithm by reversing the shift

# Main function to interact with the user
def caesar_cipher():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        print("Encrypted message: ", encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted message: ", decrypt(message, shift))
    else:
        print("Invalid choice, please try again.")

# Call the main function
if __name__ == "__main__":
    caesar_cipher()
