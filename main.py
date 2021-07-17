
from dbQuerys import dbQuerys
from UserFaker import UserFaker


if __name__ == "__main__":
    for i in range(10):
        user_faker = UserFaker()

        cardID = user_faker.get_cardID()
        prename = user_faker.get_prename()
        surname = user_faker.get_surname()
        username = user_faker.get_username(prename, surname)
        email = user_faker.get_email(prename, surname)
        birthDate = user_faker.get_birthDate()
        sex = user_faker.get_sex()
        validityDate = user_faker.get_validityDate()
        state = user_faker.get_state()
        rights = user_faker.get_rights()
        street = user_faker.get_street()
        postcode = user_faker.get_postcode()
        city = user_faker.get_city()

        print(cardID, prename, surname, username, email, birthDate, sex, validityDate, state, rights, street, postcode, city)
    #dbQuerys.addUser("6b9a0488", "svekir", "svki0001@stud.hs-kl.de", "Sven", "Kirtz", "1994-06-14", "male", "2021-01-01", "active", "Lorem Ipsum", "user", "virginiastr 14c", "66482", "zweibrücken")