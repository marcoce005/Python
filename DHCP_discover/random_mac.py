import random

def rand_mac():
    return "\\x%02x\\x%02x\\x%02x\\x%02x\\x%02x\\x%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

mac = "\xff" + "66"
print(mac)