from faker import Faker
import random
from random import randrange
from unidecode import unidecode
from lorem_text import lorem
import uuid
import time
import loading_bar

def generate_users():
    n_users = 100000
    main_dir = ""

    # to detect duplicates
    card_ids = set()
    email_shorts = set()

    # sets for random results
    localizations = ["de_DE", "fr_FR", "en_US", "es_ES"]
    sexes = ["male", "female", "diverse"]
    states = ["active", "inactive", "banned"]
    rights = ["user", "admin"]
    
    # init faker
    localization_index = randrange(len(localizations)-1)
    
    faker = Faker(localizations[localization_index])
    faker_adress = Faker("de_DE")

    # init time
    start_time = time.time()

    print("starting users generator...")
    with open(f"{main_dir}csvs/users.csv", "w", encoding="utf-8") as dest:
            dest.write(f"cardID,username,email,prename,surname,birthDate,sex,validityDate,state,note,rights,street,postcode,city")
            
            for i in range(n_users):
                cardID = str(uuid.uuid4()).replace("-", "")[:14]

                prename = faker.first_name()
                surname = faker.last_name()

                username = prename[:3] + surname[:3]
                
                email_name = prename[:2] + surname[:2]
                email_number = "00" + str(randrange(10)) + str(randrange(9) + 1)
                email_short = email_name + email_number
                while email_short in email_shorts:
                    email_number = "00" + str(randrange(10)) + str(randrange(9) + 1)
                    email_short = email_name + email_number
                email_shorts.add(email_short)
                email_domain = "stud.hs-kl.de" if randrange(2) == 0 else "hs-kl.de"
                email = email_short + "@" + email_domain

                birthDate = faker.date()

                sex_index = randrange(len(sexes))
                sex = sexes[sex_index]

                validityDate = faker.date_between(start_date="-1y")

                state_index = randrange(len(states))
                state = states[state_index]

                rights_index = randrange(len(rights))
                rights = rights[rights_index]

                street = faker_adress.street_address()

                postcode = faker_adress.postcode()

                city = faker_adress.city()

                note = ""
                if random.random() < 0.2:
                    words = randrange(1, 15)
                    note = lorem.words(words)

                dest.write(f"{cardID},{username},{email},{prename},{surname},{birthDate},{sex},{validityDate},{state},{note},{rights},{street},{postcode},{city}\n")
                loading_bar.print_loading_bar(current=i, max=n_users)
                
    end_time = time.time()
    print()
    print(f"finished in {int((end_time - start_time) / 60)} minutes!")