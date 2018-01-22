# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 17:35:19 2018

@author: Ayami
"""

from users import User

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
