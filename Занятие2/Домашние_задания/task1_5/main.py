from string import ascii_lowercase, ascii_uppercase, digits
import random
def password_():
    needed_types = ascii_lowercase + ascii_uppercase + digits
    password = random.sample(needed_types, 8)
    return "".join(password)

if __name__ == "__main__":
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    print(password_())
