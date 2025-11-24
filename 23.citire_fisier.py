# "r" - "read"
# "w" - "write"
# "a" - "append"


## V1 CITIRE FISIER - invechita
file_handler = open("22.preturi.txt", "r")
text = file_handler.read()
print(text)
print("type(text)", type(text))
file_handler.close()

## V2 -  CITIRE FISIER - recomandata
with open("22.preturi.txt", "r") as file_handler:
    text = file_handler.read()
    print(text, "type(text)", type(text))
