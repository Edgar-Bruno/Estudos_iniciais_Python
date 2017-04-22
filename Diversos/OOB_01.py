#!/usr/bin/python
# -*- coding: utf-8 -*-

class Employee(object):

	raise_amt = 1.04

	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.email = (fname + '.' + lname + '@company.com').lower()
		self.pay = pay

	def fullName(self):
		return '{} {}'.format(self.fname, self.lname)

	def appli_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

	def __init__(self, fname, lname, pay, prog_lang):
		super(Developer, self).__init__(fname, lname, pay)
		# Solução explicada em :
		# http://stackoverflow.com/questions/222877/what-does-super-do-in-python
		#Employee.__init__(self, fname, lname, pay) # Herança
		self.prog_lang = prog_lang


dev = Developer('Edgar', 'Bruno', 152400, 'Python') # Instacia da classe Employee
emp2 = Employee('Vivi', 'Nicolao', 572400)

#print (Employee.fullName(Employee('Vivi', 'Nicolao', 572400))) # Acessando a classe Employee diretamente

print (dev.prog_lang)
print (emp2.fname)
"""

emp_2 = Employee()

emp_2.fname = 'Vivi'
emp_2.lname = 'Nicolao'
emp_2.email = 'vivi@company.com'
emp_2.pay = 82000

print (emp_2)"""