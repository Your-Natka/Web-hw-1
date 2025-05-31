from views.base import BaseView

class ConsoleView(BaseView):
    def display_message(self, message: str):
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)


