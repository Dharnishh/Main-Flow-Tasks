# encrypt message script

def encrypt_caesar(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_message += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message
#example message
message = "Hi Dinesh How Are You?"
shift = 3
encrypted_message = encrypt_caesar(message, shift)
print("Encrypted message:", encrypted_message)

#decrypt message script

def decrypt_caesar(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_message += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            elif char.isupper():
                decrypted_message += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_message += char
    return decrypted_message

#example message
decrypted_message = decrypt_caesar(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
