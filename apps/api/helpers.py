from django.core.exceptions import ValidationError


def extract_backpack_id(value):
    """
    Extract the last four chars of given string. Allow only values in the format: "myswissalps.ch/rucksack/7g8h".
    :return: string
    """
    message = 'Invalid format of the backpack_url'
    try:
        elements = value.split('/')
    except AttributeError:
        raise ValidationError(message)

    try:
        if not all([
            validate_length(*elements),
            validate_domain(elements[0]),
            validate_slug(elements[1]),
            validate_backpack_id_length(elements[2])
        ]):
            raise ValidationError(message)
    except IndexError:
        raise ValidationError(message)

    return elements[-1]


def validate_length(*elements):
    return len(elements) == 3


def validate_domain(domain):
    return domain == 'myswissalps.ch'


def validate_slug(slug):
    return slug == 'rucksack'


def validate_backpack_id_length(id):
    return len(id) == 4
