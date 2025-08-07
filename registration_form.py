# Taking user input for Name, Email, and Password
Name = input('Please Enter your Name: ')
gmail = input('Please Enter your Email-id: ')
password = input('Enter your Password:(at least 6 letters)')

# Creating an empty dictionary to store user details
Dict = {}

# Function to check if the email is valid
def gmail_checker(gmail):
    # Email should contain '@', '.', and no spaces
    if '@' in gmail and '.' in gmail and ' ' not in gmail:
        return True
    return False

# Function to check if the password has at least 6 characters
def password_length_checker(password):
    if len(password) >= 6:
        return True
    return False

# Storing the result of validation functions
is_email_checker = gmail_checker(gmail)
is_password_checker = password_length_checker(password)

# If both email and password are valid
if is_email_checker and is_password_checker:
    # Add user details to the dictionary
    Dict['Name'] = Name
    Dict['Email'] = gmail
    Dict['Password'] = password
    print('Registration is Successful')
    print('User data:', Dict)
else:
    # If email is invalid
    if not is_email_checker:
        print('Invalid Email-id')
    # If password is too short
    if not is_password_checker:
        print('The length of password must be at least 6')
