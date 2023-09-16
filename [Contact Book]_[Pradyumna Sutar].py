#Contact Book
# Initialize an empty contact book dictionary and a Sequence order for contact IDs
contacts_list = {} # using dictionary : Gaddis Python 6e Chapter 09
num_contact = 1

#  A function to display the main contact book options

def display_menu(): # Ref Defining and Calling a Function
    print("Digital Contact Book: E-contacts")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Show stored contacts")
    print("5. Exit")

# When the program's execution ends, contacts are stored to a text file and loaded from the file when the programmes begins.
def store_the_contacts_textfile(): 
    with open("contacts_list.txt", "a") as file: # Using the with Statement to Open File : Gaddis Python 6e Chapter 06
        for num_contact, contacts_details in contacts_list.items():
            file.write(f"Contact ID: {num_contact}\n")
            file.write(f"Name: {contacts_details['Name']}\n")
            file.write(f"Email: {contacts_details['mail-ID']}\n")
            file.write(f"Phone: {contacts_details['Mobi']}\n")
            file.write("\n")


# Continuous loop for displaying  contact book option
while True:
    display_menu() # Reference Defining and Calling a Function 
    choice = input("Enter your decision: ")

    if choice == "1":
        print("Enter the Details\n")
        name = input("Enter the contact name: ")
        email = input("Enter the contact mail ID: ")
        phone = input("Enter the Mobile Number: ")

        # Generate a unique ID for contact
        contact_numid = num_contact
        num_contact += 1

        # Add contact to the contact list
        contacts_list[contact_numid] = {"Name": name, "mail-ID": email, "Mobi": phone} # mixing data types in dictionary : Gaddis Python 6e Chapter 09

        print(f"Contact '{name}' has been added to the e-contact.")

        # Store the updated contacts to the text file
        store_the_contacts_textfile() # Defining and Calling a Function from Gaddis Python 6e Chapter 05

    # view the entered contact information
    elif choice == "2":
        print("View Contact info:")
        for num_contact, contacts_details in contacts_list.items(): # Nested loops concept from Gaddis Python 6e Chapter 05
            print("Contact ID:", num_contact)
            print("Name:", contacts_details["Name"])
            print("Email:", contacts_details["mail-ID"])
            print("Phone:", contacts_details["Mobi"])
            print()

    # To find the contact, by providing the contact name
    elif choice == "3":
        name = input("Enter the name you are searching for: ")
        contact = None
        for num_contact, contacts_details in contacts_list.items():
            if contacts_details["Name"] == name:
                contact = contacts_details
                break
        try: # exception handler : Gaddis Python 6e Chapter 06
            if contact:
                print(f"Name: {name}")
                print(f"Phone: {contact['Mobi']}")
                print(f"Email: {contact['mail-ID']}")
            else:
                raise ValueError()  # Raise an exception if the contact is not found
        except ValueError:
            print(f"Contact '{name}' not found in the contact book.")

    # Shows the previouly stored Contacts
    elif choice == "4":
        with open("contacts_list.txt", "r") as file: # files : Gaddis Python 6e Chapter 06
            content = file.read()
            print(content)

    elif choice == "5":
        print("Exit the program")
        break  # exit the loop 

    else:
        print("The selected option is not available right now. Please choose a valid option from the menu.")
