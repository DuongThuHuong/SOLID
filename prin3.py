class Calculator():
    def calculate(self, a, b): #always returns a number
        return a * b

class DividerCalculator(Calculator):
		def calculate(self, a, b):
			return a / b          


calculation_results = [
    Calculator().calculate(3, 4),
    Calculator().calculate(5, 7),
	DividerCalculator().calculate(3, 4),
	DividerCalculator().calculate(5, 0)
]

print(calculation_results)

#### liskov substituion principle ######


class Calculator():
    def calculate(self, a, b): #always returns a number
        return a * b

class DividerCalculator(Calculator):
	try:
		def calculate(self, a, b):
			return a / b           #try except code
	except ZeroDivisionError:
		print("b is different from 0. Enter back b ")


calculation_results = [
    Calculator().calculate(3, 4),
    Calculator().calculate(5, 7),
	DividerCalculator().calculate(3, 4),
	DividerCalculator().calculate(5, 0)
]

print(calculation_results)

#---- Refactoring the class hierarchy -----#