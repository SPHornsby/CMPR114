# The get_login_name fucntion accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.


def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the first name is less than 3 characters, the
    # slice will return the entire first name.
    set1 = first[0 : 3]

    # Get the first three letters of the last name.
    # If the last name is less than 3 characters, the
    # slice will return the entire last name.
    set2 = last[0 : 3]

    # Get the last three letters of the student ID.
    # If the student ID is less than 3 characters, the
    # slice will return the entire student ID.
    set3 = idnumber[-3 :]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name

# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. A valid
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.

# This function has some simple tests. Run pytest or pytest -v
# to test.
def valid_password(password: str):
    # Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing the
    # password's length.
    if len(password) >= 7:
        correct_length = True

        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
    
    if correct_length and has_uppercase and \
        has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    return is_valid