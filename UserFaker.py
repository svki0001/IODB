from faker import Faker
import random
import string
from random import randrange
from unidecode import unidecode

class UserFaker:
    faker = None
    faker_adress = None

    n_users = 0

    card_ids = set()
    email_shorts = dict()

    sexes = ["male", "female", "diverse"]
    states = ["active", "inactive", "banned"]
    rights = ["user", "admin"]
    localizations = ["de_DE", "fr_FR", "en_US", "es_ES"]

    def __init__(self) -> None:
        # init faker
        localization_index = randrange(len(self.localizations)-1)
        
        self.faker = Faker(self.localizations[localization_index])
        self.faker_adress = Faker("de_DE")
        self.prename = self.get_prename()
        self.surname = self.get_surname()

    # cardID: Studentenkarten ID. Kann sich ändern.
    def get_cardID(self):
        card_id = ""
        card_id_added = False
        while not card_id_added:
            card_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
            if card_id not in self.card_ids:
                self.card_ids.add(card_id)
                card_id_added = True
        return card_id

    # Username: Wird aus den ersten drei Buchstaben vom Vor- und Nachnamen erzeugt. Kann der Benutzer später selbst ändern. 
    def get_username(self):
        username = self.prename[:3] + self.surname[:3]
        return unidecode(username).lower()

    # Email: Studenten oder Mitarbeiter-Email. Ändert sich im System der Hochschule eigentlich nicht.
    def get_email(self):
        email_name = self.prename[:2] + self.surname[:2]
        email_name = unidecode(email_name).lower()
        if email_name in self.email_shorts.keys():
            self.email_shorts[email_name] += 1
        else:
            self.email_shorts[email_name] = 1
        email_number = f"{self.email_shorts[email_name]:04d}"
        email_short = email_name + email_number
        email_domain = "stud.hs-kl.de" if randrange(1) == 0 else "hs-kl.de"
        return email_short + "@" + email_domain

    # Vorname
    def get_prename(self):
        return self.faker.first_name()

    # Nachname
    def get_surname(self):
        return self.faker.last_name()

    # Geburtsdatum
    def get_birthDate(self):
        return self.faker.date()

    # Geschlecht
    def get_sex(self):
        sex_index = randrange(len(self.sexes))
        return self.sexes[sex_index]

    # Datum der ersten Registrierung
    def get_validityDate(self):
        return self.faker.date_between(start_date="-2y")

    # Active: Registriert und Bezahlt; Inactive: Registriert, aber noch nicht bezahlt; Banned: Aus dem Sportraum gebannt
    def get_state(self):
        state_index = randrange(len(self.states))
        return self.states[state_index]

    # User: Normaler Benutzer; Admin: Darf im Sportraum das System neustarten, etc.
    def get_rights(self):
        rights_index = randrange(len(self.rights))
        return self.rights[rights_index]

    # Adresse: Straße + Hausnummer
    def get_street(self):
        return self.faker_adress.street_address()

    # PLZ
    def get_postcode(self):
        return self.faker_adress.postcode()

    # Stadt
    def get_city(self):
        return self.faker_adress.city()