import datetime
import webbrowser

class Jarvis:
    def __init__(self):
        self.commands = {
            "time": self.get_time,
            "date": self.get_date,
            "search": self.search_web,
            "exit": self.exit
        }

    def get_time(self):
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    def get_date(self):
        return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"

    def search_web(self, query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"I've opened a web search for '{query}'"

    def exit(self):
        print("Goodbye!")
        exit()

    def process_command(self, command):
        command_parts = command.lower().split(maxsplit=1)
        command_key = command_parts[0]

        if command_key in self.commands:
            if command_key == "search" and len(command_parts) > 1:
                return self.commands[command_key](command_parts[1])
            elif command_key != "search":
                return self.commands[command_key]()
        else:
            return "I'm sorry, I don't understand that command."

def main():
    jarvis = Jarvis()
    print("Hello! I'm your personal assistant. How can I help you?")
    
    while True:
        user_input = input("Command: ")
        response = jarvis.process_command(user_input)
        print(response)

if __name__ == "__main__":
    main()