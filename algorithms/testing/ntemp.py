data_set = {
    'allentran': {
        'name': 'allen',
        'home': '/bin/allen',
        'shell': '/bash'
    },
    'jcolumbres': {
        'name': 'julian',
        'home': '/bin/julian',
        'shell': '/NoShell'
    },
    'patrick': {
        'name': 'patrick',
        'home': '/bin/patrick',
        'shell': '/bash'
    },
}


class ManageUser:
    def __init__(self):
        self.user_list = []
        self.distinct_user = set()

    def parse(self, data_set):
        pass

    def add_user(self, username, name, home, shell):
        if username in self.distinct_user:
            raise "Username already taken"

        if not name:
            name = "DEFAULT"
        if not home:
            home = '/bin/default'
        if not shell:
            shell = '/bash'

        self.distinct_user.append([username, name, home, shell])
        
    def print_users(self):
        self.user_list.sort(key=lambda x: x[0])

        for user in self.user_list:
            pass

'''
TEST
'''

user_manager = ManageUser()
user_manager.add_user('juliancolumbres', 'julian', '/bin/home', '/bash')
user_manager.print_users()