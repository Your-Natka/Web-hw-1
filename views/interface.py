from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def display_contacts(self, contacts: str):
        pass

    @abstractmethod
    def display_notes(self, notes: str):
        pass

    @abstractmethod
    def display_commands(self, commands: dict):
        pass

    @abstractmethod
    def display_message(self, message: str):
        pass

    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass

