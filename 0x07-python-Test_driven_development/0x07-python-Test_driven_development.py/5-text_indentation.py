#!/usr/bin/python3

def text_indentation(text):
    """
    Function prints a text with 2 new line after each of these character . ? :

    Args
     text(str): sting 

    Raises
     TypeError: if text is not a string 
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    H = 0

    while H < len(text) and text[H] == ' ':
        H += 1

    while H < len(text):
        print(text[H], end="")

        if text[H] == "\n" or text[H] in ".?:":
            if text[H] in ".?:":
                print("\n")
            H += 1
            while H < len(text) and text[H] == ' ':
                H += 1
            continue

        H += 1