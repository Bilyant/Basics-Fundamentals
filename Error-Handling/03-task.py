class NameTooShortError(Exception):
    ...


class MustContainAtSymbolError(Exception):
    ...


class InvalidDomainError(Exception):
    ...


def validate_domain(domain_str: str):
    is_valid = False
    for valid_domain in valid_domains:
        if domain_str.endswith(valid_domain):
            is_valid = True
            break
    return is_valid


line = input()
valid_domains = ['.com', '.bg', '.org', '.net']

while line != 'End':
    email = line
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    name, right_part = email.split('@')
    if len(name) < 5:
        raise NameTooShortError('Name must be more than 4 characters')
    _, domain = right_part.split('.')
    is_domain_valid = validate_domain(domain)
    if not is_domain_valid:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    print('Email is valid')
    line = input()
