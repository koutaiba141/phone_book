import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date

cred = credentials.Certificate("c:\\Users\\Koutaiba\\Downloads\\project-1-koutaiba-firebase-adminsdk-nzlvv-531316c928.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
contacts = db.collection('contacts')
def num_add(number,name):
    d = date.today().strftime("%Y-%m-%d")
    contacts.add({
        'phone': number,
        'name' : name,
        'date' : d
    })
    print(f'name: {name} phone: {number} date: {d} added')

def s_n_num(number):
    for records in contacts.stream():
        if records.to_dict()['phone'] == number:
            return records.to_dict()['name']
        else:
            return 'number not found'
def s_n_name(name):
    for records in contacts.stream():
        if records.to_dict()['name'] == name:
            return records.to_dict()['phone']
        else: 
            return 'name not found'
def delete_contact(number):
    # Query for documents with the given phone number
    query = contacts.where('phone', '==', number).get()
    
    # Delete the documents that match the query
    for doc in query:
        doc.reference.delete()

    print(f"{len(query)} contact(s) with phone number {number} deleted")

def display_all():
    for records in contacts.stream():
        data = records.to_dict()
        print(f"Name: {data['name']}, Phone: {data['phone']}, Date: {data['date']}")

def change_name(new_name, phone):

    query = contacts.where('phone', '==', phone).get()
    
    for doc in query:
        doc.reference.update({'name': new_name})

    print(f"Updated name to '{new_name}' for contact(s) with phone number {phone}")

def change_number(new_number, name):
    query = contacts.where('name', '==', name).get()
    
    for doc in query:
        doc.reference.update({'phone': new_number})

    print(f"Updated phone number to '{new_number}' for contact(s) with name '{name}'")

def main():
    while True:
        print("\nOptions:")
        print("1. Add a new contact")
        print("2. Search contact by phone number")
        print("3. Search contact by name")
        print("4. Display all contacts")
        print("5. Change name")
        print("6. Change number")
        print("7. Delete contact")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            number = input("Enter phone number: ")
            name = input("Enter name: ")
            num_add(number, name)
        elif choice == '2':
            number = input("Enter phone number: ")
            print(s_n_num(number))
        elif choice == '3':
            name = input("Enter name: ")
            print(s_n_name(name))
        elif choice == '4':
            display_all()
        elif choice == '5':
            number = input("Enter phone number: ")
            new_name = input("Enter new name: ")
            change_name(new_name, number)
        elif choice == '6':
            name = input("Enter name: ")
            new_number = input("Enter new phone number: ")
            change_number(new_number, name)
        elif choice == '7':
            number = input("Enter phone number to delete: ")
            delete_contact(number)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")



main()

