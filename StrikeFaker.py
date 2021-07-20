from lorem_text import lorem
from random import randrange

n_strikes = int(100000 * 0.15)

#main_dir = "IODB/"
main_dir = ""

with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
    dest.write(f"strikeID,sessionID,description")
    for i in range(n_strikes):
        strikeID = "NaN"
        sessionID = "NaN"
        count = randrange(5, 15)
        desc = lorem.words(count)
        
        dest.write(f"\n{strikeID},{sessionID},{desc}")