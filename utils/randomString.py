import random
import string


def random_email_generate(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_password_generate(size=5, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))
