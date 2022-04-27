import requests
import random
import string
import json
import os


# setting variables
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))


# setting up different domain extensions
domain = ['.com', '.gov', '.us', '.edu', '.org', '.ru', '.tw', ]

# url to overflow
#url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php']
url = 'https://www.stealmylogin.com/demo.html'

# loading and reading json files
names = json.loads(open('names.json').read())
org = json.loads(open('domain.json').read())

# setting up random users and password
for name in names:
    name_extra = ''.join(random.choice(string.digits))
    # username = name.lower() + name_extra + '@' + random.choice(org) + random.choice(domain)
    # password = ''.join(random.choice(chars) for i in range(8))
    userId = name.lower() + name_extra + '@' + random.choice(org) + random.choice(domain)
    userPassword = ''.join(random.choice(chars) for i in range(8))

# sending user/password to url above
    requests.post(url, allow_redirects=False, data={
        # 'auid2yjauysd2uasdasdasd': username,
        # 'kjauysd6sAJSDhyui2yasd': password
        'auid2yjauysd2uasdasdasd': userId,
        'kjauysd6sAJSDhyui2yasd': userPassword
    })



# print the results  - example: sending username noah8@HIPHOP.edu and password ankCRzk8
    # print('sending username %s and password %s' % (username, password))
    print('sending username %s and password %s' % (userId, userPassword))