# Create an empty list to store data
user_data = []

# Define a valid name to only accept alphabet with at least 1 character
def valid_name(name):
    return name.isalpha() and len(name) > 0
# Define a valid age to only accept positive integer ranging 1-120
def valid_age(age):
    return age.isdigit() and 0 < int(age) <= 120

# Create a loop that asks user for name and age
while True:
    # Use try and except to validate the datas
    try:     
        # Ask user to input a name
        name = input("Enter name: ")    
        # Raise an error if the name is invalid, ask user to input an alphabet
        if not valid_name(name):
            raise  ValueError ("Invalid character, Please input an alphabet")
        # Ask user to input age
        age = input("Enter age: ")
        # Raise an error if the age is invalid, ask user to input positive integer from 1-120
        if not valid_age(age):
            raise ValueError ("Invalid character, Please input an integer(1-120)")  

        # Store data in list
        user_data.append((name, int(age)))
        
    except ValueError as error:
        print(error)

#Ask user if they want to input another data
    another_entry = input("Do you want to input another entry? (Yes/No): ")
# Break if the user input no
    if another_entry.lower() == "no":
        break
# Print error message if the user input neither yes nor no
    elif another_entry.lower() != "yes":
     print("Invalid entry, Try again")

# Create an empty list to store oldest person
if user_data:
        oldest_person = []
# Set the oldest age to zero
        oldest_age = 0
# Set the name and age as user
        for user in user_data:
            name, age = user        
# Identify and compare if the user's age is older than the current oldest
            if age > oldest_age:
                oldest_age = age
                # Reset the oldest person if there is a new oldest person
                oldest_person = [user]
            # Store all the oldest person in list
            elif age == oldest_age:
                oldest_person.append(user)
# Display the oldest person/s
        for user in oldest_person:
            name, age = user
            print("The oldest person/s:", name, "age:", age)
# Print error message if there is no age input
else:
    print("Invalid. No user data available")


