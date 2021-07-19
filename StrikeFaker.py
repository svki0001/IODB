from lorem_text import lorem

n_strikes = int(100000 * 0.15)

#main_dir = "IODB/"
main_dir = ""

with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
    dest.write(f"strikeID,sessionID,description\n")
    for i in range(n_strikes):
        strikeID = "NaN"
        sessionID = "NaN"
        desc = lorem.sentence()
        
        dest.write(f"{strikeID},{sessionID},{desc}\n")