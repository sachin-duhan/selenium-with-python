import names
import random

class User():
    f = names.get_first_name()
    l = names.get_last_name()
    n = random.randint(10, 100)

myUser = User()
form_val = {'firstName': myUser.f, 'lastName': myUser.l,
        'email': myUser.f + myUser.l + str(myUser.n) + '@gmail.com' , 'password': 'password'}

for key in form_val:
    print(key, '->', form_val[key])
