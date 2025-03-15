# Morse Code Converter by Mohammed Thamim Ahmed
# Task: You will use what you've learnt to create a text-based 
# (command line) program that takes any String input and converts it into 
# Morse Code.

# The Python skill this shows: Python scripting

# The Morse code itself
morse_code = {
    "A": " .- ",
    "B": " -... ",
    "C":" -.-. ",
    "D":" -.. ",
    "E":" . ",
    "F":" ..-. ",
    "G":" --. ",
    "H":" .... ",
    "I":" .. ",
    "J":" .--- ",
    "K":" -.- ",
    "L":" .-.. ",
    "M":" -- ",
    "N":" -. ",
    "O":" --- ",
    "P":" .--. ",
    "Q":" --.- ",
    "R":" .-. ",
    "S":" ... ",
    "T":" - ",
    "U":" ..- ",
    "V":" ...- ",
    "W":" .-- ",
    "X":" -..- ",
    "Y":" -.-- ",
    "Z":" --.. ",

    "1":" .---- ",
    "2":" ..--- ",
    "3":" ...-- ",
    "4":" ....- ",
    "5":" ..... ",
    "6":" -.... ",
    "7":" --... ",
    "8":" ---.. ",
    "9":" ----. ",
    "0":" ----- ",
    " ":" ",
}

# Conversion from string to morse code
def converter(user_input):
    try:

# For loop prints code respective to their charcters in the string
# Can add end = "" to print on the same line
        for characters in user_input:
            print(morse_code[characters])
    except:
        print("Enter a Valid input")

# Start of program
user_input = input("Enter a string of letters and numbers: ").upper()
print("Morse code below:")
converter(user_input)