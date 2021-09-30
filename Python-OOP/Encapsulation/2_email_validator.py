class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = set(mails)
        self.__domains = set(domains)

    def validate(self, email):
        name = ''
        mail = ''
        domain = ''
        return self.__validate_name(name) \
               and self.__validate_mail(mail) \
               and self.__validate_domain(domain)

    def __validate_name(self, name):
        return name and self.__min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.__mails

    def __validate_domain(self, domain):
        return domain in self.__domains
