class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.first_name = user_id
        self.last_name = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

    

 
users = [User(23), User(3), User(99)]
print(users)
# [User(23), User(3), User(99)]
print(sorted(users, key=lambda u: u.user_id))
# [User(3), User(23), User(99)]
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))
# [User(3), User(23), User(99)]
 


by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
print(by_name)
# [User(3), User(23), User(99)]

print(min(users, key=attrgetter('user_id')))
# User(3)
print(max(users, key=attrgetter('user_id')))
# User(99)
