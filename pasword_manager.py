from cryptography.fernet import Fernet
import os
import sys

# Function to generate and save a key (only done once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    
# Function to load the key from the file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a password
def encrypt_password(password):
    key = load_key()  # Load the key
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()  # Load the key
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to store a password securely
def store_password(service, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.txt", "a") as file:
        file.write(f"{service} | {encrypted_password.decode()}\n")

# Function to retrieve a password securely
def retrieve_password(service):
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_service, encrypted_password = line.strip().split(" | ")
            if stored_service == service:
                return decrypt_password(encrypted_password.encode())
    return None

# Main function to interact with the user
def main():
    # Check if key file exists, if not, generate a new key
    if not os.path.exists("key.key"):
        print("Key file not found. Generating a new key...")
        generate_key()

    while True:
        print("Password Manager Menu:")
        print("1. Store a password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the name of the service (e.g., Google, Facebook): ")
            password = input("Enter the password: ")
            store_password(service, password)
            print(f"Password for {service} stored successfully!")

        elif choice == "2":
            service = input("Enter the name of the service to retrieve the password: ")
            retrieved_password = retrieve_password(service)
            if retrieved_password:
                print(f"Password for {service}: {retrieved_password}")
            else:
                print(f"No password found for {service}")

        elif choice == "3":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
