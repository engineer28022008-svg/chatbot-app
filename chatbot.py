from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Simple chatbot logic
def bot_reply(user_text):
    user_text = user_text.lower()

    greetings = ["hi", "hello", "hey"]
    questions = ["how", "what", "why", "when"]
    
    if any(word in user_text for word in greetings):
        return "Hello 😊 How can I help you?"

    if "your name" in user_text:
        return "I am a smart chatbot 🤖"

    if "how are you" in user_text:
        return "I am always good 😄"

    if any(word in user_text for word in questions):
        return "That's a good question 🤔 I'm learning to answer better."

    if "bye" in user_text:
        return "Goodbye 👋 Have a nice day!"

    return "I didn't fully understand, but I'm learning 📚"


class MyChatbotApp(App):

    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Scroll area for chat
        scroll = ScrollView()
        self.chat_box = BoxLayout(orientation="vertical", size_hint_y=None)
        self.chat_box.bind(minimum_height=self.chat_box.setter("height"))
        scroll.add_widget(self.chat_box)

        # Input area
        input_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.text_input = TextInput(hint_text="Type message...", multiline=False)
        send_btn = Button(text="Send")
        send_btn.bind(on_press=self.send_message)

        input_layout.add_widget(self.text_input)
        input_layout.add_widget(send_btn)

        main_layout.add_widget(scroll)
        main_layout.add_widget(input_layout)

        return main_layout

    def send_message(self, instance):
        user_text = self.text_input.text.strip()
        if user_text == "":
            return

        # Show user message
        self.chat_box.add_widget(
            Label(text=f"You: {user_text}", size_hint_y=None, height=30)
        )

        # Bot reply
        reply = bot_reply(user_text)
        self.chat_box.add_widget(
            Label(text=f"Bot: {reply}", size_hint_y=None, height=30)
        )

        self.text_input.text = ""


# Run app
if __name__ == "__main__":
    MyChatbotApp().run()