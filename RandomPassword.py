import random
import string
import getpass

class PasswordGenerator:
    def __init__(self):
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.symbols = string.punctuation

    def generate_password(self, length):
        """
        Generate a random password of a given length
        using a combination of letters, numbers, and symbols
        """
        all_characters = self.letters + self.numbers + self.symbols
        password = ''.join(random.choice(all_characters) for _ in range(length))

        # Ensure the password has at least one character from each set
        while (not any(c.isalpha() for c in password) or
               not any(c.isdigit() for c in password) or
               not any(c in self.symbols for c in password)):
            password = ''.join(random.choice(all_characters) for _ in range(length))

        return password

    def get_password_length(self):
        """
        Prompt the user to enter a password length
        """
        while True:
            try:
                length = int(input("Enter the password length (min 8 characters): "))
                if length < 8:
                    print("Password length must be at least 8 characters.")
                else:
                    return length
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_username(self):
        """
        Prompt the user to enter a username
        """
        return input("Enter a username: ")

    def save_password(self, username, password):
        """
        Save the generated password to a file
        """
        with open("passwords.txt", "a") as f:
            f.write(f"{username}:{password}\n")
        print(f"Password saved for {username}.")

    def main(self):
        username = self.get_username()
        length = self.get_password_length()
        password = self.generate_password(length)
        print(f"Generated password: {password}")
        self.save_password(username, password)

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.main()
