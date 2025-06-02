from views.interface import Interface

class ConsoleInterface(Interface):

    def display_contacts(self, contacts: str):
        print("Contacts:\n" + contacts)

    def display_notes(self, notes: str):
        print("Notes:\n" + notes)

    def display_commands(self, commands: dict):
        print("Available commands:")
        for cmd in commands:
            print(f"- {cmd}")

    def display_message(self, message: str):
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)
