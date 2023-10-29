import json

# Load the JSON data
with open('data1123.json', 'r') as file:
    data = json.load(file)

# User input
user_input = input("Enter NIM: ")

try:
    user_input = int(user_input)
    # Search for the NIM value in the data
    for entry in data:
        if entry.get("NIM") == user_input:
            # If a matching entry is found, print all the values
            print("Data Found:")
            for key, value in entry.items():
                print(f"{key}: {value}")
            break
    else:
        # If no matching entry is found
        print("Data not found")
except ValueError:
    # If the user input is not an integer
    print("Invalid input. Please enter an integer NIM.")