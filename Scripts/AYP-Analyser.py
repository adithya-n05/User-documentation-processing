import requests
import argparse
import json

headers = {
    'x-api-key': 'ask_f3aa063182fcda8c62f80973f01088b4'
}

parser = argparse.ArgumentParser(description="Chatbot for user documentation assistance",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--path", type=str, help="Name of pdf in the same directory as this script that you would like to process.")
args = parser.parse_args()
config = vars(args)
print(config)

FilePath = config["path"]

file_data = open(FilePath, 'rb')

response = requests.post('https://api.askyourpdf.com/v1/api/upload', headers=headers,
 files={'file': file_data})

if response.status_code == 201:
    print(response.json())
else:
    print('Error:', response.status_code)

headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'ask_f3aa063182fcda8c62f80973f01088b4'
}

docid = response.json()

data = [
    {
        "sender": "user",
        "message": "Hello!"
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
        data.append({"sender":"user", "message": message})
    else:
        while message == "":
            message = input("The system does not accept an empty message, please write something: ")