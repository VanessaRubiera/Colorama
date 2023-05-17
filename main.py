from art import *
from colorama import init, Fore, Back, Style
init()

print(Fore.MAGENTA + "El profe de ") # some text in color magenta
print(Back.CYAN + "Python ") # some text with background color cyan
print(Back.YELLOW + "rifa.")
print(Style.RESET_ALL) # to reset text to normal

aprint("butterfly") # print a ascii draw