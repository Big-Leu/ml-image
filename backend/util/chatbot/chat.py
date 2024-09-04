import random
import json

import torch
from util.chatbot.nltk_utils import tokenize, bag_of_words
from util.chatbot.model import NeuralNet
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open("E:/Git-Hub/Personal/ml-image/backend/util/chatbot/intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "E:/Git-Hub/Personal/ml-image/backend/util/chatbot/data.pth"
data = torch.load(FILE, weights_only=True)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"


def get_response(msg):
    # flag = 0
    # latitude = 0
    # longitude = 0
    # str2 = ""
    # if "&" in msg:
    #     words = msg.split("&")
    #     if len(words) > 1:
    #         words2 = words[1].split(",")
    #         if len(words2) == 2:
    #             latitude = float(words2[0])
    #             longitude = float(words2[1])
    #         else:
    #             print("Invalid format for latitude and longitude.")
    #     else:
    #         print("No latitude and longitude found after splitting.")
    # else:
    #     print("No '&' found in the msg.")
    #     str2 = msg
    #     flag = 1

    # str = location_check(latitude, longitude)
    # sentence = ""
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent["responses"])

    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)
