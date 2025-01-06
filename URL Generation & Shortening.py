from urllib.parse import urlparse
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False
    
original_url = input("Please input original url: ")
print("Checking the url:")
storage = {}
if uri_validator(original_url):
    print("The url is valid")
    short_url = "http://bism.com/" + id_generator(size = 6)
    print("The short url is: ", short_url)
    storage[short_url] = original_url


print("Lets retrieve the original url")
input_short_key = input("Enter the short url: ")
print("Retrieving long URL for key:", input_short_key)
print("Original URL:", storage.get(input_short_key, "Key not found"))


#Try to make it written to a file or a database