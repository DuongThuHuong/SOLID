class Book:

	def __init__(self, name, ID, author):
		self.name = name
		self.ID = ID
		self.author = auhor
 	
	# returns string represenation
	def str(self): 
		return 'Book({},{},{})'.format(self.author, self.name, self.ID)
	
	#determines if book itself equivalent to the book by checking if all three instance variables are the same.
	def eq(self, other):
		return self.name == other.name and self.author == other.author and self.ID == ID
	 
	#display name of book
	def displayName(self):
		print(self.name)

###### Single Responsibility Principle #######

# Contains only book information
class Book:
	
	def __init__(self, name, ID, author):
		self.name = name
		self.ID = ID
		self.author = author

# Display book
class DisplayBook(Book):
	
	def getName(self):
	   	Print(self.name)

#equivalent
class Equivalent(Book):
	
	def eq(self, other):
		return self.name == other.name and self.author == other.author and self.ID == ID
