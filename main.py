
from dbQuerys import dbQuerys
from UserFaker import UserFaker
import time

note = "note"
nbr_users = 100000
start_time = 0
end_time = 0

#main_dir = "IODB/"
main_dir = ""

def print_loading_bar(i, len_bar=16):
    i = int((i / nbr_users) * len_bar)
    bar = "\u2593" * i + "\u2591" * (len_bar - i)
    print(bar, end="\r")

if __name__ == "__main__":
    # generate users
    with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
        dest.write(f"cardID,username,email,prename,surname,birthDate,sex,validityDate,state,note,rights,street,postcode,city")
        print("starting generator...")
        start_time = time.time()
        for i in range(1, nbr_users+1):
            user_faker = UserFaker()

            cardID = user_faker.get_cardID()
            prename = user_faker.prename
            surname = user_faker.surname
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
            print_loading_bar(i)
            #print(cardID, prename, surname, username, email, birthDate, sex, validityDate, state, rights, street, postcode, city)
        end_time = time.time()
        print()
        print(f"finished in {int((end_time - start_time) / 60)} minutes!")
    #dbQuerys.addUser("6b9a0488", "svekir", "svki0001@stud.hs-kl.de", "Sven", "Kirtz", "1994-06-14", "male", "2021-01-01", "active", "Lorem Ipsum", "user", "virginiastr 14c", "66482", "zweibrücken")