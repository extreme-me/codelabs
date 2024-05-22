# Define a function to generate email addresses
def generate_email(name):
    # Split the name into first and last names
    names = name.split()
    if len(names) == 1:
        first_name, last_name = names[0], ''
    else:
        first_name, last_name = names[0], names[1]

    # Generate the email address
    email = f'{first_name.lower()}{last_name.lower()}@gmail.com'

    # Check if the email address is unique
    if email in email_addresses:
        i = 1
        while f'{first_name.lower()}{last_name.lower()}{i}@gmail.com' in email_addresses:
            i += 1
        email = f'{first_name.lower()}{last_name.lower()}{i}@gmail.com'

    # Add the email address to the list
    email_addresses.append(email)

    # Return the email address
    return email

# Initialize an empty list to store email addresses
email_addresses = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Generate the email address for each student
    student_name = row['Student Name']
    email = generate_email(student_name)
    print(f'Student Name: {student_name} - Email address: {email}')
def generate_character_email():
    pass


def read_email_file():
    pass

