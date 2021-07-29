from database.dbQuerys import update_user_note, update_user_rights_by_right, update_user_rights_by_cardID, select_cardids_by_rights
import pandas as pd
import random

# Params
main_dir = "IODB/"
ermahnt = "Ermahnt"
n_admins = 10
n_ermahnt = 1000

# cardIDs laden
users =  pd.read_csv(f"{main_dir}csvs/users.csv")
cardIDs = set(users["cardID"])

# Alle User rights zu "user"
update_user_rights_by_right("user", "admin")

# Random Admin generieren
randomCardIDs = random.sample(cardIDs, n_admins)
for cardID in randomCardIDs:
    update_user_rights_by_cardID("admin", cardID)

# Random Admin ermahnen
randomAdminCardID = randomCardIDs[random.randint(0, n_admins-1)]
update_user_note(ermahnt, randomAdminCardID)

# Random Ermahnungen generieren
data = select_cardids_by_rights("user")
randomCardIDs = random.sample(data, n_ermahnt)
for row in randomCardIDs:
    update_user_note(ermahnt, row["cardID"])