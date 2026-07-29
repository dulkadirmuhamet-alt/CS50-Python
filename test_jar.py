import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

available_fonts = figlet.getFonts()



if len(sys.argv) == 1:
    selected_font = random.choice(available_fonts)
    figlet.setFont(font=selected_font)



elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in available_fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

user_input = input("Input: ")





print("Output:" )

print(figlet.renderText(user_input))
