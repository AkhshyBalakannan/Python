''' This is user profile module'''


class User():
    '''This is an user class for user module'''
    user_count = 0

    def __init__(self, first_name, last_name, password, amount=0):
        '''This is init function which creates the instance of the class'''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.amount = amount
        self.user_count += 1

    def full_name(self):
        return f'{self.first_name}{self.last_name}'

    def user_id(self):
        return f'{self.first_name}{self.user_count}'


if __name__ == '__main__':
    users = User('akhshy', 'ganesh', 'hash')
    users.full_name()
    print(users.user_id())
    print(users.amount)
