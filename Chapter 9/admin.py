# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 15:39:18 2018

@author: Ayami
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:35:54 2017

@author: Ayami
"""

#Assignment 9.7: Admin
class User(object):
    """Gives summary of user information."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initialises the first name and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempt = 0
    
    def describe_user(self):
        """Prints a summary of the user info."""
        print("\nUser info: ")
        print("\nName: " + self.first_name.title() + " " + self.last_name.title()  )
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.location.title())
       
    def greet_user(self):
        """Greets the user."""
        print("\nGood day, " + self.username + " !")
        
    def login_attempts(self):
        print("\nLogin Attempts: " + str(self.login_attempt) )
        
    def increment_login_attempts(self):
        self.login_attempt += 1
        
    def reset_login_attempts(self):
        if self.login_attempt >= 1:
            self.login_attempt = 0
            print("Resetting login attempts..")
        else:
            print("The number of attempts is already 0 !")
            
class Admin(User):
    """An admin is a special user, with more privileges."""
    def __int__(self, first_name, last_name, username, email, location):
        super(Admin, self).__init__(first_name, last_name, username, email, location)
        self.privileges = []
        
    def show_privileges(self):
        """prints a list of the admin's privileges"""
        print("\n What would you like to do ?")
        for privilege in self.privileges:
            print("- " + privilege)
        
user_1 = User('ayami', 'nakajo', 'anakajo', 'ayami@email.com', 'osaka')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.login_attempts()
user_1.reset_login_attempts()
user_1.login_attempts()

user_2 = User('yua', 'shinkawa', 'yshinkawa', 'yua@email.com', 'tokyo')
user_2.describe_user()
user_2.greet_user()

user_3 = User('rena', 'matsui', 'rmatsui', 'rena@email.com', 'nagoya')
user_3.describe_user()
user_3.greet_user()

user_admin = Admin('rina', 'takahashi', 'admin', 'rtakahashi@email.com', 'shibuya')
user_admin.privileges = ['add post', 'delete post', 'ban user', 'check user info', 'modify theme']
user_admin.describe_user()
user_admin.show_privileges()
