from database.dbQuerys import dbQuerys
import time

nbr_users = 9768
nbr_log_users = 100000
start_time = 0
end_time = 0

main_dir = ""
#main_dir = "IODB/"

cardIDs = set()

def print_loading_bar(current, len_bar=16, max=nbr_users):
    i = int((current / max) * len_bar)
    bar = "\u2593" * i + "\u2591" * (len_bar - i)
    print(bar + " " + str(current) + " of " + str(max), end="\r")

def generateFakeUsers():
    from generator.UserFaker import UserFaker
    # generate users
    #with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
        #dest.write(f"cardID,username,email,prename,surname,birthDate,sex,validityDate,state,note,rights,street,postcode,city")

            #dest.write(f"{cardID},{username},{email},{prename},{surname},{birthDate},{sex},{validityDate},{state},{note},{rights},{street},{postcode},{city}\n")
            #print(cardID, prename, surname, username, email, birthDate, sex, validityDate, state, rights, street, postcode, city)

    print("starting generator...")
    start_time = time.time()
    for i in range(1, nbr_users+1):
        user_faker = UserFaker()

        cardID = user_faker.get_cardID()
        while cardID not in cardIDs:
            cardID = user_faker.get_cardID()
            cardIDs.add(cardID)
            
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

        dbQuerys.addUser(cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city)
        print_loading_bar(i, max=nbr_users)

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
<<<<<<< HEAD
    generateFakeUsers()
    # generateContracts()

    # START HERE
    # generateUserNotes()
    #import database.dbImport as dbImport
    # dbImport.import_users
    # generateLogUsers()
    # dbImport.import_log_users
=======
    # generate data
    # generateFakeUsers()
    # generateUserNotes()
    # generateContracts()
    # generateLogUsers()
>>>>>>> main
    # generateStrikes()

<<<<<<< HEAD
    # dbImport.import_contracts
    
    # CONTINUE HERE
    
    
    
    
    
=======
    # import data
    import database.dbImport as dbImport
    # dbImport.import_users
    # dbImport.import_log_users
    # dbImport.import_contracts()
    dbImport.import_strikes()
>>>>>>> main
