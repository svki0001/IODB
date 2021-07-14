from faker import Faker
import random
import re

localizations = [
    "de_DE",
    # "hi_IN",
    "fr_FR",
    # "ja_JP",
    "en_US",
    "es_ES",
    # "ru_RU"
]


fake_adress = Faker("de_DE")

for i in range(10):
    idx = random.randint(0, len(localizations)-1)
    fake_name = Faker(localizations[idx])
    name = fake_name.name().replace("Prof.", "").replace("B.A.", "").replace("Dr.", "").replace("MBA.", "").replace("B.Sc.", "").replace("B.Eng.", "").strip()
    
    adress = fake_adress.address()
    adress = adress.replace("/", "")
    
    if adress.split(" ")[-1] == "0\n":
        nbr = random.randint(1, 200)
        adress = adress.replace("0", str(nbr))

    print(name)
    print(adress)