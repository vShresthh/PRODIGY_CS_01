def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts a text using the Caesar Cipher.

  Args:
    text: The text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: The mode of operation, either 'encrypt' or 'decrypt'.

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  
  for char in text:
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char
  return result

if __name__ == "__main__":
  text = input("Enter your message: ")
  shift = int(input("Enter the shift value (1-25): "))
  mode = input("Enter mode (encrypt/decrypt): ")

  if mode == 'encrypt':
    encrypted_text = caesar_cipher(text, shift, mode)
    print("Encrypted text:", encrypted_text)
  elif mode == 'decrypt':
    decrypted_text = caesar_cipher(text, -shift, mode)
    print("Decrypted text:", decrypted_text)
  else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
