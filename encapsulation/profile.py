class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        if 5 <= len(username) <= 15:
            self.__username = username

        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        upper_case = [character for character in password if character.isupper()]
        lower_case = [x for x in password if x.islower()]
        number_present = [y for y in password if y.isdigit()]
        if upper_case and lower_case and number_present and len(password) >= 8:
            self.__password = password

        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username","Passw0rd")

print(correct_profile)


