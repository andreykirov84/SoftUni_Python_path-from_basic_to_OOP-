class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ['com', 'bg', 'org', 'net']


line = input()
while line != 'End':
    if len(line.split('@')[0]) < 5:
        raise NameTooShortError('Name must be more than 4 characters')
    elif '@' not in line:
        raise MustContainAtSymbolError('Email must contain @')
    elif line.split('@')[-1].split('.')[-1] not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    else:
        print('Email is valid')

    line = input()

