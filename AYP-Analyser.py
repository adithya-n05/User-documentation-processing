import requests
import argparse
import json
import logging
from datetime import datetime

headers = {
    'x-api-key': 'ask_237416234388a431ea38de6834218df1'
}

parser = argparse.ArgumentParser(description="Chatbot for user documentation assistance",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--path", type=str, help="Name of pdf in the same directory as this script that you would like to process.")
args = parser.parse_args()
config = vars(args)
print(config)

FilePath = config["path"]

print("Opening file...")
file_data = open(FilePath, 'rb')

print("Communicating with AYP servers...")
response = requests.post('https://api.askyourpdf.com/v1/api/upload', headers=headers,
 files={'file': file_data})

print("Response received, decoding document ID...")
if response.status_code == 201:
    print(response.json())
else:
    print('Error:', response.status_code)

headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'ask_237416234388a431ea38de6834218df1'
}

docid = response.json()

data = [
    {
        "sender": "user",
        "message": "You are a chat assistant made to help corporate banking customers learn how to use our corporate banking products. We have passed to you our user documentation. At any point, if a user asks a question that you are unable to provide an answer to, or they are not in the provided context, please respond to those queries with \"I apologise, I do not know the response to that question, please contact tagit@gmail.com if you have any further queries.\". The user will also not understand if you respond with answers such as \"based on the provided context...\" or other such responses, as the user will only be seeing an interface to talk to you, they are not aware of the fact that your responses are based on the pdf that has been passed to you. If you understand all these requirements, please return to this query \"Hello! Welcome to the Mobeix Chat assistant\""
    }
]
message = " "

print("Welcome! Feel free to ask any queries regarding the document to this bot. If you would like to finish speaking, please type \"bye\"")

while message != "bye":
    if message != "":
        response = requests.post('https://api.askyourpdf.com/v1/chat/' + docid['docId'] + '?stream=True', headers=headers, data=json.dumps(data))
        response.raise_for_status()
        responsestrval = ""
        print("System: ", end="")
        for chunk in response.iter_content(chunk_size=24):
            chunk_str = chunk.decode('utf-8')
            print(chunk_str, end="")
            responsestrval = responsestrval + chunk_str
        data.append({"sender": "bot", "message": responsestrval})
        message=input("\nUser: ")
        if message == "bye":
            print("System: See you later!")
            data.append({"sender": "user", "message": "bye"})
            data.append({"sender": "bot", "message": "See you later!"})
        data.append({"sender":"user", "message": message})
    else:
        while message == "":
            message = input("The system does not accept an empty message, please write something: ")
    
