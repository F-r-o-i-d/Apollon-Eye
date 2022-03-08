from operator import imod


import colorama, os
colorama.init()
color = {"red":colorama.Fore.LIGHTRED_EX,
        "blue":colorama.Fore.LIGHTBLUE_EX,
        "green":colorama.Fore.GREEN,
        "magenta":colorama.Fore.LIGHTMAGENTA_EX,
        "clear":colorama.Fore.LIGHTWHITE_EX,
        "desc":colorama.Fore.LIGHTBLACK_EX,
        "category": colorama.Fore.LIGHTCYAN_EX,
        "module": colorama.Fore.LIGHTRED_EX}
def alert(text, stop=False):
    print(color["red"] + " [ ! ] " + color["clear"] + "- " + text + color["clear"])
    if stop:
        exit(1)

def info(text):
    print(color["blue"] + "\t [ ! ] " + color["clear"] + text)


def FormatText(text):
    printable_text = ""
    text = text.split("%%")

    for x in text:
        if x == "desco":
            printable_text += color["desc"]
        elif x == "descc":
            printable_text += color["clear"]
        else:
            printable_text += x
    return printable_text
def FormatTextList(text):
    printable_text = ""
    text = text.split("\n")
    for d in text:
        d = str(d).split("/")
        for x in range(len(d)):
            if x == 0:
                printable_text += color["category"]
                printable_text += d[x]
                printable_text += color["clear"] + "/"
            elif x == 1:
                printable_text += color["module"]
                printable_text += d[x]
                printable_text += color["clear"]
    return printable_text

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        print('\x1bc')
def success(text):
    print(color["green"] + " [ + ] " + color["clear"] + "- " + str(text) + color["clear"])

