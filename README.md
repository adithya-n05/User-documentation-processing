# User documentation chatbot for Tagit

## Introduction

This is a chatbot that helps users to find the right information about Tagit. It is built using AYP and openai, an API that generates text based on the input file you provide it. The chatbot is hosted on a server and can be accessed through the link below.

## Description:

The folder consists of the following files:
1. AYP-analyser.py - This is the main file that contains the code for the chatbot. It is written in python and uses the openai and AYP API to generate text based on the input file.


## Installation:

1. Clone the repository
2. Install the requirements using the command:

```zsh
pip install -r requirements.txt
```

## Usage:

Ensure that any files you would like to be analysed are stored in the same directory as the analyser file.

To run the analyser, use the command:

```zsh
python AYP-analyser.py -p PATHTOFILE
```
## Debugging:

Logs are stored under a folder called logs. The logs are stored in a file named Logs-CURRENTTIME-FILEANALYSED.log. The logs are stored in a .log file format and the outputs of the communication with the chatbot can be viewed here.