
import re
import random
import hashlib

test_base_url = "http://0.0.0.0:5000"

LICENSE_REGISTERED = "registered"
LICENSE_UNREGISTERED = "unregistered"
LICENSE_WRONG_CLUSTER = "wrong_cluster"
LICENSE_DOESNT_EXIST = "doesnt_exist"
LICENSE_KEY = b'Py10izoC3bApB5UChCjgqYRMbEFS5yG94BUfMoQ_XU8='

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
NULL_PARAMS = "Parameters can't be null"
INVALID_FORMAT = "Wrong parameter format"


def gen_salt():
    return "".join(random.choice(ALPHABET) for i in range(16))


def validate_email(email):
    return EMAIL_REGEX.match(email)