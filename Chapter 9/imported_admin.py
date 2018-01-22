# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 17:24:24 2018

@author: Ayami
"""

import privileges as pv

user_admin = pv.Admin('rina', 'takahashi', 'admin', 'rtaka@email.com', 'shibuya')
user_admin.describe_user()
user_admin.privilege.privileges = ['add post', 'ban post', 'ban user']
user_admin.privilege.show_privileges()
