# reading = open("output.txt", "r")
# text = reading.read()
# reading.close()

def paddingCode(text: str):
    return text.replace('/', '_')

def reverseCode(code: str):
    return code.replace('_', '/')

# with open("output.txt", "w") as writing:
#     writing.write(reverseCode(text))