import re

def moss_signal(data: str):
    result = ''
    code ={'.-': 'A', '-...':'B', '-.-.' : 'C', '-..': 'D', '.':'E', '..-.' : 'F',
           '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
           '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
           '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
           '-.--': 'Y', '--..': 'Z', '': ' '
           }
    for moss in data.split(' '):
        print(moss)
        result += code[moss]
    print(result)

if __name__ == '__main__':
    moss_signal('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--')
