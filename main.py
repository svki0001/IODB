
from Log_Users_Faker import Log_Users_Faker
from dbQuerys import dbQuerys
from UserFaker import UserFaker
import time
from datetime import datetime

note = "note"
nbr_users = 100000
nbr_log_users = 10
start_time = 0
end_time = 0

#main_dir = "IODB/"
main_dir = ""

def print_loading_bar(i, len_bar=16, max=nbr_users):
    i = int((i / max) * len_bar)
    bar = "\u2593" * i + "\u2591" * (len_bar - i)
    print(bar, end="\r")

def createFakeUserCSV():
    # generate users
    with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
        dest.write(f"cardID,username,email,prename,surname,birthDate,sex,validityDate,state,note,rights,street,postcode,city\n")
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

def createFakeLogUsersCSV():    # generate users
    with open(f"{main_dir}csvs/log_users.csv", "w", encoding="utf-8") as dest:
        dest.write(f"cardID,sessionID,checkIn,checkOut\n")
        print("starting generator...")
        start_time = time.time()
        for i in range(1, nbr_log_users+1):
            log_users_faker = Log_Users_Faker()

            cardID = log_users_faker.get_cardID()
            checkIn = log_users_faker.get_checkIn()
            checkOut = log_users_faker.get_checkOut(checkIn)
            
            checkInStr = checkIn.strftime("%Y.%m.%d %H:%M:%S")
            checkOutStr = checkOut.strftime("%Y.%m.%d %H:%M:%S")

            dest.write(f"{cardID},,{checkInStr},{checkOutStr}\n")
            print_loading_bar(i=i, max=nbr_log_users)


        end_time = time.time()
        print()
        print(f"finished in {int((end_time - start_time) / 60)} minutes!")


if __name__ == "__main__":
    #dbQuerys.addUser("6b9a0488", "svekir", "svki0001@stud.hs-kl.de", "Sven", "Kirtz", "1994-06-14", "male", "2021-01-01", "active", "Lorem Ipsum", "user", "virginiastr 14c", "66482", "zweibrücken")
    #createFakeUserCSV()
    createFakeLogUsersCSV()
