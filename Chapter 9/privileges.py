# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 15:54:19 2018

@author: Ayami
"""

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
            
class Privilege(object):
    """presents the privileges available for an admin."""
    def __init__(self):
        self.privileges = []
        
    def show_privileges(self):
        """prints a list of the admin's privileges"""
        print("\n What would you like to do ?")
        for privilege in self.privileges:
            print("- " + privilege)
            
class Admin(User):
    """makes a unique admin user with its own privileges"""
    def __init__(self, first_name, last_name, username, email, location):
        super(Admin, self).__init__(first_name, last_name, username, email, location)
        self.privilege = Privilege()
        
user_admin = Admin('rina', 'takahashi', 'rtakahashi', 'rtaka@email.com', 'shibuya')
user_admin.describe_user()
user_admin.privilege.privileges = ['add post', 'remove post', 'ban user']
user_admin.privilege.show_privileges()
