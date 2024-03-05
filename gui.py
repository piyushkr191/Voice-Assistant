# import tkinter as tk
# from tkinter import scrolledtext
# from threading import Thread
# import time
# import random
# import json
# import torch
# from brain import NeuralNet
# from NeuralNetwork import bag_of_words, tokenize
# from task import (
#     Time, Date, Commandprompt, NoninputExecution, Wikipedia, Google, InputFunction
# )

# class AIChatbotGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("AI Chatbot")
#         self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # Define self.device here
#         self.load_chatbot_model()
#         self.create_gui()
#         self.all_words = None

# # ... Other methods ...


#     def load_chatbot_model(self):
#     # Load your chatbot model, data, and other components here.
#     # Example:
#         device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#         with open('intents.json', 'r') as f:
#             self.intents = json.load(f)

#         FILE = "TrainData.pth"
#         data = torch.load(FILE)

#         input_size = data["input_size"]
#         hidden_size = data["hidden_size"]
#         output_size = data["output_size"]
#         self.all_words = data["all_words"]
#         self.tags = data["tags"]  # Define self.tags here
#         model_state = data["model_state"]

#         self.model = NeuralNet(input_size, hidden_size, output_size).to(device)
#         self.model.load_state_dict(model_state)
#         self.model.eval()




#     def process_input(self):
#         user_input = self.input_entry.get()
#         self.input_entry.delete(0, 'end')
#         self.update_chat("You: " + user_input)

#         # Call your chatbot logic to generate a response here and store it in the 'response' variable.
#         # Example:
#         response = self.chatbot_response(user_input)

#         # Update the chat history with the chatbot's response.
#         self.update_chat("AI: " + response)

#     def create_gui(self):
#     # Create and configure the GUI elements such as labels, text input, and buttons.
#         self.input_label = tk.Label(self.root, text="User Input:")
#         self.input_label.pack()

#         self.input_entry = tk.Entry(self.root)
#         self.input_entry.pack()

#         self.send_button = tk.Button(self.root, text="Send", command=self.process_input)
#         self.send_button.pack()

#         self.chat_history = scrolledtext.ScrolledText(self.root, width=40, height=10)
#         self.chat_history.pack()

#     # You can add more GUI elements as needed.

#     # Start the main loop.
#         self.root.mainloop()


#     def chatbot_response(self, user_input):
#     # Your chatbot logic here.
#     # Modify your existing AI code to provide responses based on user input.

#     # Example:
#         sentence = user_input
#         netSearch = str(sentence)

#         if sentence == "good bye":
#             exit()
#         sentence = tokenize(sentence)
#         X = bag_of_words(sentence, self.all_words)  # Use self.all_words here
#         X = X.reshape(1, X.shape[0])
#         X = torch.from_numpy(X).to(self.device)

#         output = self.model(X)
#         _, predicted = torch.max(output, dim=1)
#         tag = self.tags[predicted.item()]  # Use self.tags here

#         probs = torch.softmax(output, dim=1)
#         prob = probs[0][predicted.item()]

#         if prob.item() > 0.75:
#             for intent in self.intents["intents"]:
#                 if tag == intent["tag"]:
#                     reply = random.choice(intent["responses"])

#                 # Modify to handle different responses based on intent.
#                 # Example: You can call NoninputExecution, InputFunction, or Say functions here.

#                     return reply

#     # Default response if no intent matches.
#         return "I'm sorry, I didn't understand that."


#     def update_chat(self, message):
#         self.chat_history.insert(tk.END, message + "\n")
#         self.chat_history.see(tk.END)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AIChatbotGUI(root)
#     root.mainloop()
import nltk
nltk.download('wordnet')