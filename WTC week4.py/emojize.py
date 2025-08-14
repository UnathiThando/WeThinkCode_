from emoji import emojize , is_emoji
import sys
string= input("Enter collon before and after emoji name: ").strip().lower()

# When the user forgets to put a collon
if not string.startswith(":"):
    string= ":" + string
if not string.endswith(":"):
    string= string + ":"
    
emojize_string = emojize(string , language="alias")
#When the name of emoji is not available

if not is_emoji(emojize_string):
    sys.exit("Invalid emoji name. Please try again.")
print(f"Hello, {emojize_string}")
