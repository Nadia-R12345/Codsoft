import re
import random
from datetime import datetime

# Nadia's ChatBot (spec)
# I built a simple chatbot that responds to user inputs based on
# predefined words to identify basic user questions and use premade responses.

# if user input contains common greeting word, Nadbot chooses a random return welcome response
def handle_greeting(user_input):
    if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
        welcome = [
            "Hello there!",
            "Hi, how can I help you?",
            "Hey! What's up?",
            "Greetings! How may I assist?"
        ]
        return random.choice(welcome)
    return None

# if user input contains exit term, Nadbot outputs exit response prior to closing
def handle_farewell(user_input):
    if re.search(r'\b(bye|exit|q|quit|goodbye)\b', user_input):
        return "Goodbye! It was nice talking to you, you know you can always chat again!"
    return None

# returns the bot name if user types 'your name'
def handle_bot_name(user_input):
    if "your name" in user_input:
        return "I'm NadBot"
    return None

# returns a random response from the mood list if user types 'how are you'
def handle_how_are_you(user_input):
    if "how are you" in user_input:
        mood = [
            "Im well! Thanks for asking!",
            "Bad, cause you're here ...",
            "Why? Would it help you to know?",
            "Fine."
            "...",
            "Happy, and happy to help! Any other questions?"
        ]
        return random.choice(mood)
    return None

# returns the current time from datetime library
def handle_time(user_input):
    if "time" in user_input:
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    return None

# returns the current date from datetime library
def handle_date(user_input):
    if "date" in user_input:
        today = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {today}."
    return None

# returns a random response from the joke list when user asks for a joke (took jokes from https://www.moserit.com/blog/best-tech-jokes)
def handle_joke(user_input):
    if "joke" in user_input:
        jokes = [
            "What kind of computer sings the best? A Dell.",
            "Why did the developer become so poor? Because he cleared his cache.",
            "What made the Java developers wear glasses? They can't C.",
            "How many programmers does it take to change a light bulb? None, because it is a hardware problem."
            "Why do they call it hyper text? Too much JAVA.",
            "Have you heard of that new band 1023 Megabytes? They're pretty good, but they don't have a gig just yet."
        ]
        return random.choice(jokes)
    return None

# shows all programmed NadBot response types if user wants options on NadBot capabilities
def handle_help(user_input):
    if "help" in user_input:
        return (
            "Here's what I can do:\n"
            "- Say hi \n"
            "- Responds to 'your name' or 'how are you'\n"
            "- Can tell you the 'time' or 'date'\n"
            "- Tells jokes\n"
            "- Say bye (to exit)"
        )
    return None

# unhandled input
def handle_fallback(user_input):
    return "Thats currently not within something I can answer. Type 'help' to see what I can do."

# uses parts of user input to assign to the associated function for handling / output
def get_response(user_input):
    user_input = user_input.lower().strip()

    handlers = [
        handle_greeting,
        handle_farewell,
        handle_bot_name,
        handle_how_are_you,
        handle_time,
        handle_date,
        handle_joke,
        handle_help
    ]

    for handler in handlers:
        response = handler(user_input)
        if response:
            return response

    return handle_fallback(user_input)

# maintains main and loop to prevent incorrect repetiton
# of introduction statement and maintain loop correctly until exit
if __name__ == "__main__":
    print("Hello! I'm your friendly chatbot, NadBot. Type 'help' for options on what to write or 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("NadBot: ", response)
        if re.search(r'\b(bye|exit|q|quit|goodbye)\b', user_input.lower()):
            break
