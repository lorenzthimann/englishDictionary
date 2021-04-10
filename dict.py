
import json
import difflib
d = json.load(open("data.json"))

def print_def(l):
    if len(l) == 1:
        print("Definition:")
        print(l[0])
    else:
        print("Definitions: ")
        for i in range(len(l)):
            print(f"{i + 1}. {l[i]}")

stop = False
while not stop:
    ipt = input("Give me a word and I'll give u its definition: (or type /s to stop): ").lower()
    if ipt == "/s":
        stop = True
    elif ipt in d.keys():
        definition = d[ipt]
        if len(definition) == 1:
            print("Definition:")
            print(definition[0])
        else:
            print("Definitions: ")
            for i in range(len(definition)):
                print(f"{i + 1}. {definition[i]}")
    else:
        # cant find word
        close = difflib.get_close_matches(ipt, d.keys())
        if close == []:
            print("Sorry, we could not find the word you are looking for.")
        else:
            ask = input(f"Did u mean {close[0]} ? [y / n]: ").lower()
            if ask == "y":
                definition = d[close[0]]
                print_def(definition)
    print()


