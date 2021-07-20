import time

nbr_users = 100000
nbr_log_users = 100000
start_time = 0
end_time = 0

main_dir = ""
#main_dir = "IODB/"

def print_loading_bar(i, len_bar=16, max=nbr_users):
    i = int((i / max) * len_bar)
    bar = "\u2593" * i + "\u2591" * (len_bar - i)
    print(bar, end="\r")

def generateFakeUsers():
    from generator.UserFaker import UserFaker
    # generate users
    with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
        dest.write(f"cardID,username,email,prename,surname,birthDate,sex,validityDate,state,note,rights,street,postcode,city")
        print("starting generator...")
        start_time = time.time()
        for i in range(1, nbr_users+1):
            user_faker = UserFaker()

            cardID = user_faker.get_cardID()
            prename = user_faker.get_prename()
            surname = user_faker.get_surname()
            username = user_faker.get_username()
            email = user_faker.get_email()
            birthDate = user_faker.get_birthDate()
            sex = user_faker.get_sex()
            validityDate = user_faker.get_validityDate()
            state = user_faker.get_state()
            note = user_faker.get_note()
            rights = user_faker.get_rights()
            street = user_faker.get_street()
            postcode = user_faker.get_postcode()
            city = user_faker.get_city()

            dest.write(f"{cardID},{username},{email},{prename},{surname},{birthDate},{sex},{validityDate},{state},{note},{rights},{street},{postcode},{city}\n")
            print_loading_bar(i, max=nbr_users)
            #print(cardID, prename, surname, username, email, birthDate, sex, validityDate, state, rights, street, postcode, city)

        end_time = time.time()
        print()
        print(f"finished in {int((end_time - start_time) / 60)} minutes!")

def generateLogUsers():    # generate users
    from generator.LogUsersFaker import LogUsersFaker
    with open(f"{main_dir}csvs/log_users.csv", "w", encoding="utf-8") as dest:
        dest.write(f"cardID,checkIn,checkOut")
        print("starting generator...")
        start_time = time.time()
        for i in range(1, nbr_log_users+1):
            log_users_faker = LogUsersFaker()

            cardID = log_users_faker.get_cardID()
            checkIn = log_users_faker.get_checkIn()
            checkOut = log_users_faker.get_checkOut(checkIn)
            
            checkInStr = checkIn.strftime("%Y-%m-%d %H:%M:%S")
            checkOutStr = checkOut.strftime("%Y-%m-%d %H:%M:%S")

            dest.write(f"{cardID},{checkInStr},{checkOutStr}\n")
            print_loading_bar(i=i, max=nbr_log_users)


        end_time = time.time()
        print()
        print(f"finished in {int((end_time - start_time) / 60)} minutes!")

def generateContracts():
    from generator.ContractFaker import ContractFaker
    cf = ContractFaker()
    cf.generateContracts()
    
def generateStrikes():
    from generator.StrikeFaker import StrikeFaker
    sf = StrikeFaker()
    sf.generateStrikes()

    
def generateUserNotes():
    from generator.UserNotesFaker import UserNotesFaker
    uf = UserNotesFaker()
    uf.generateUserNotes()

if __name__ == "__main__":
    # generateFakeUsers()
    # generateContracts()

    # START HERE
    # generateUserNotes()
    generateLogUsers()
    # generateStrikes()

    # CONTINUE HERE
    import database.dbImport as dbImport
    # dbImport.import_users
    # dbImport.import_log_users
    # dbImport.import_contracts
    # dbImport.import_strikes