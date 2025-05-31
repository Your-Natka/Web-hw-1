from abc import ABC, abstractmethod

class BaseView(ABC):
    @abstractmethod
    def display_message(self, message: str):
        pass

    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass

   
