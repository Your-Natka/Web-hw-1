from utility import input_error
from storage import load_data, save_data
from modul8.address_book import AddressBook
from modul8.fields import Name, Phone, Birthday
from modul8.record import Record
from views.console import ConsoleInterface # ✅ нове
from commands import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    clear_book,
    exit_program,
)

view = ConsoleInterface()  

@input_error
def parse_command(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    book = load_data()
    view.display_message("Welcome to the assistant bot!")

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
        "clear": clear_book,
        "hello": lambda args, book: "How can I help you?",
    }

    while True:
        user_input = view.get_input("Enter a command: ").strip()
        if not user_input:
            continue
        command, args = parse_command(user_input)

        if command in ["close", "exit"]:
            view.display_message(exit_program(args, book))
            break

        handler = commands.get(command)
        if handler:
            try:
                result = handler(args, book)
                if result is not None:
                    view.display_message(result)
            except Exception as e:
                view.display_message(f"Error: {e}")
        else:
            view.display_message("Invalid command.")

if __name__ == "__main__":
    main()
