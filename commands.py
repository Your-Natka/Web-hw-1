from modul8.fields import Name, Phone, Birthday
from modul8.record import Record
from storage import save_data
from modul8.address_book import AddressBook

def add_contact(args, book):
    name, phone = args
    record = book.get(name)
    if record:
        record.add_phone(Phone(phone))
        return f"Phone {phone} added to contact {name}."
    else:
        record = Record(Name(name))
        record.add_phone(Phone(phone))
        book.add_record(record)
        return f"Contact {name} with phone {phone} added."

def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.get(name)
    if record:
        record.edit_phone(Phone(old_phone), Phone(new_phone))
        return f"Phone number for {name} updated from {old_phone} to {new_phone}."
    else:
        return f"Contact {name} not found."

def show_phone(args, book):
    name = args[0]
    record = book.get(name)
    if record:
        phones = ', '.join(str(p) for p in record.phones)
        return f"{name}: {phones}"
    else:
        return f"Contact {name} not found."

def show_all(args, book: AddressBook):
    if not book:
        return "Address book is empty."
    result = []
    for record in book.values():
        phones = ', '.join(str(p) for p in record.phones)
        birthday = record.birthday.value if record.birthday else "No birthday"
        result.append(f"{record.name.value}: {phones}; Birthday: {birthday}")
    return '\n'.join(result)

def add_birthday(args, book: AddressBook):
    name, bday = args
    record = book.get(name)
    if record:
        record.add_birthday(Birthday(bday))
        return f"Birthday {bday} added for {name}."
    else:
        return f"Contact {name} not found."

def show_birthday(args, book: AddressBook):
    if not args:
        return "Please provide a contact name."
    name = args[0]
    record = book.get(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value}"
    else:
        return f"No birthday found for {name}."

def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays this week."
    result = []
    for person in upcoming:
        result.append(f"{person['name']}: {person['birthday']}")
    return '\n'.join(result)

def clear_book(args, book: AddressBook):
    book.clear()
    save_data(book)
    return "Address book cleared."

def exit_program(args, book: AddressBook):
    save_data(book)
    return "Goodbye!"
