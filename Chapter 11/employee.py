# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 18:58:16 2018

@author: Ayami
"""

import unittest

class Employee(object):
    def __init__(self, first_name, last_name, annual_salary):
        """Initialises employee attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.new_raise = new_raise
    
    def give_raise(self, new_raise = 5000):
        """Adds raise to employee's annual salary"""
        if self.new_raise:
            self.new_raise = new_raise
            self.annual_salary += self.new_raise
            return self.annual_salary
        else:
            self.annual_salary += 5000
            return self.annual_salary

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""
    
    def setUp(self):
        """Create an set employee for all test methods."""
        self.my_employee = Employee('rina', 'takahashi', 15000)
    
    def test_give_default_raise(self):
        """Expected outcome: '2000'"""
        new_salary = self.my_employee.give_raise()
        self.assertEqual(new_salary, 20000)
        
    def test_give_custom_raise(self):
        """Expected outcome '1600'"""
        new_salary = self.my_employee.give_raise(1000)
        self.assertEqual(new_salary, 16000)
        
unittest.main()
