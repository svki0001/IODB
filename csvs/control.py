import pandas as pd

main_dir = ""
main_dir = "IODB/"

users = pd.read_csv(f"{main_dir}csvs/users.csv")
log_users = pd.read_csv(f"{main_dir}csvs/log_users.csv")
contracts = pd.read_csv(f"{main_dir}csvs/contracts.csv")

u_cardIDs = users["cardID"]
l_cardIDs = log_users["cardID"]

u_emails = users["email"]
c_emails = contracts["email"]

u_cardIDs = set(u_cardIDs)
l_cardIDs = set(l_cardIDs)
u_emails = set(u_emails)
c_emails = set(c_emails)

# duplicates = False
# for u_cardID in u_cardIDs:
#     if u_cardID not in l_cardIDs:
#         duplicates = True
#         break
# print(f"users duplicates: {duplicates}")
    
duplicates = False
for u_email in u_emails:
    if u_email not in c_emails:
        duplicates = True
        break
print(f"email duplicates: {duplicates}")
