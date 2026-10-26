from contact import *

FILENAME = 'contacts.txt'


def readSalary(prompt):
    # keeps asking until a valid whole number is entered
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Salary must be a number. Try again.')


def findContact(contacts, fname, sname):
    for index in range(len(contacts)):
        if contacts[index].getFname() == fname and contacts[index].getSname() == sname:
            return index
    return None


def addContact(contacts):
    fname = input('First Name: ')
    sname = input('Surname: ')
    if findContact(contacts, fname, sname) is not None:
        print('Contact already exists.')
        return
    desig = input('Designation: ')
    salary = readSalary('Salary: ')
    c = Contact(fname, sname, desig, salary)
    contacts.append(c)
    print('Contact added successfully.')


def removeContact(contacts):
    fname = input('First Name: ')
    sname = input('Surname: ')
    index = findContact(contacts, fname, sname)
    if index is not None:
        del contacts[index]
        print('Contact removed successfully.')
    else:
        print('Contact not found.')


def searchContact(contacts):
    fname = input('First Name: ')
    sname = input('Surname: ')
    index = findContact(contacts, fname, sname)
    if index is not None:
        print('\n' + str(contacts[index]))
    else:
        print('Contact not found.')


def showContacts(contacts):
    if len(contacts) == 0:
        print('No contacts available.')
    else:
        print(f'{"Name":<20}{"Designation":<15}{"Salary":>10}')
        print('-' * 45)
        for c in contacts:
            print(c.getContact())


def modifyContact(contacts):
    fname = input('First Name: ')
    sname = input('Surname: ')
    index = findContact(contacts, fname, sname)

    if index is None:
        print('Contact not found.')
        return

    print('\n1. Modify First Name')
    print('2. Modify Surname')
    print('3. Modify Designation')
    print('4. Modify Salary')

    option = input('Enter modification option: ')

    if option == '1':
        contacts[index].setFname(input('New First Name: '))
    elif option == '2':
        contacts[index].setSname(input('New Surname: '))
    elif option == '3':
        contacts[index].setDesig(input('New Designation: '))
    elif option == '4':
        contacts[index].setSalary(readSalary('New Salary: '))
    else:
        print('Invalid modification option.')
        return

    print('Contact modified successfully.')


def loadContacts(contacts):
    try:
        with open(FILENAME, 'r') as f:
            loaded = []
            for line in f:
                line = line.strip()
                if line == '':
                    continue            # skip blank lines
                fname, sname, desig, salary = line.split(',')
                loaded.append(Contact(fname, sname, desig, int(salary)))
    except FileNotFoundError:
        print('No saved file found.')
        return
    except ValueError:
        print('File is corrupted. Nothing was loaded.')
        return

    contacts.clear()                    # replace, don't duplicate
    contacts.extend(loaded)
    print('Contacts loaded successfully.')


def saveContacts(contacts):
    with open(FILENAME, 'w') as f:
        for c in contacts:
            f.write(c.getFname() + ',' + c.getSname() + ',' +
                    c.getDesig() + ',' + str(c.getSalary()) + '\n')
    print('Contacts saved successfully.')


def menu():
    print('\n1. Add Contact')
    print('2. Remove Contact')
    print('3. Search Contact')
    print('4. Show All Contacts')
    print('5. Modify Contact')
    print('6. Load Contacts')
    print('7. Save Contacts')
    print('8. Exit')
    return input('Enter your choice: ')


def main():
    contacts = []

    while True:
        choice = menu()

        if choice == '1':
            addContact(contacts)
        elif choice == '2':
            removeContact(contacts)
        elif choice == '3':
            searchContact(contacts)
        elif choice == '4':
            showContacts(contacts)
        elif choice == '5':
            modifyContact(contacts)
        elif choice == '6':
            loadContacts(contacts)
        elif choice == '7':
            saveContacts(contacts)
        elif choice == '8':
            print('Program terminated.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()