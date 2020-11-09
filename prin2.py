
class vehicle:

	def __init__(self, name):
		self.name = name
	
	def cost(self):
		if self.name == 'Bycycle':
			return 4000
		elif self.name == 'Car':
			return 5000
		else:
			return 1

	
### Open/ Closed Principle #####

class Vehicle:
	
	def __init__(self, name):
		self.name = name
	
	def cost(self):
		return 1

class Bycycle(Vehicle):
	def cost(self):
		return super().cost() * 4000

class Car(Vehicle):
	def cost(self):
		return super().cost() * 5000
