#PascalCase: for every new word should have a Uppercase letter - class names
#camelCase: the first word has a lowercase letter and the subsequent words first letters are uppercase - not common in python
#snake_case: each word is separated by an underscore _ - all other name

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        #print("New user")
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    
user_1 = User("001", "John")
user_2 = User("002", "Jack")
user_1.follow(user_2)

print("1 " + str(user_1.followers))
print("1 " + str(user_1.following))
print("2 " + str(user_2.followers))
print("2 " + str(user_2.following))



