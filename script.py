
import math
import os
import sys
import requests
math
os

x = 200 * 4
print(x)

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


r = requests.get('https://google.com')

print(r.status_code)
