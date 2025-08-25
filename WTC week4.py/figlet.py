import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

try:
    if len(sys.argv) == 1:
        fonts = figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid")
except Exception:
    sys.exit("Error: invalid font")

text = input("Enter a text: ")
print(figlet.renderText(text))
