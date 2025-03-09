class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if self.min_length <= len(name):
            return True

        else:
            return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True

        else:
            return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True

        else:
            return False

    def validate(self, email):
        name = ""
        mail = ""
        domain = ""
        monkey = 0
        for i in range(len(email)):

            if email[i] == "@":
                name = email[0:i]
                monkey = i

            elif email[i] == ".":
                mail = email[monkey + 1:i]
                domain = email[i + 1::]

        return self.__is_domain_valid(domain) and self.__is_mail_valid(mail) and self.__is_name_valid(name)

mails = ["gmail", "softuni"]

domains = ["com", "bg"]

email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))

print(email_validator.validate("georgios@gmail.net"))

print(email_validator.validate("stamatito@abv.net"))

print(email_validator.validate("abv@softuni.bg"))

