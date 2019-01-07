import re

class EmailVal:

    def valFun(email):
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
            print('Valid Email ID')   
        else:
            print('Invalid Email ID')


EmailVal.valFun('abhishekmuthyam23@gmail.com')
