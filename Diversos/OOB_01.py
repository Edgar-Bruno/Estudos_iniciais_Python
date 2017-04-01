#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Employee:

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.email = (fname + '.' + lname + '@company.com').lower()
		self.pay = pay

	def fullName(self):
		return '{} {}'.format(self.fname, self.lname)

emp_1 = Employee('Edgar', 'Bruno', 152400) # Instacia da classe Employee

print (Employee.fullName(Employee('Vivi', 'Nicolao', 572400))) # Acessando a classe Employee diretamente

print (emp_1.email)

"""emp_2 = Employee()

emp_2.fname = 'Vivi'
emp_2.lname = 'Nicolao'
emp_2.email = 'vivi@company.com'
emp_2.pay = 82000

print (emp_2)"""