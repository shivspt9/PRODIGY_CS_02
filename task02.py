import os

# Fixed path
INPUT_PATH = r"C:\Users\shivt\Pictures\image1.jpeg"

# Ask user whether to encrypt or decrypt
operation = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt the image: ").strip().lower()

# Get key from user
try:
    key = int(input("Enter encryption/decryption key (0-255): "))
    if not (0 <= key <= 255):
        raise ValueError("Key must be in range 0-255.")
except ValueError as e:
    print(f"Invalid key: {e}")
    exit(1)

# Determine output file name
if operation == 'encrypt':
    output_path = r'C:\Users\shivt\Desktop\prodigy\encrypted_image.jpg'
elif operation == 'decrypt':
    output_path = r'C:\Users\shivt\Desktop\prodigy\decrypted_image.jpg'
else:
    print("Invalid operation. Choose 'encrypt' or 'decrypt'.")
    exit(1)

# XOR-based encryption/decryption
try:
    with open(INPUT_PATH, 'rb') as fin:
        data = bytearray(fin.read())

    for i in range(len(data)):
        data[i] ^= key

    with open(output_path, 'wb') as fout:
        fout.write(data)

    print(f"{operation.capitalize()}ion complete. Output saved to: {output_path}")

except Exception as e:
    print(f"Error processing image: {e}")
