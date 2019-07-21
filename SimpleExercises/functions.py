#functions and classes

def find_max(list):
	temp = 0
	for i in range(len(list)):
		if i == 0:
			temp = list[i]
		elif list[i] > temp:
			temp = list[i]
	
	return temp

list = [1, 5, 8, 7]

print(find_max(list))

class extended_val:
	value = 0
	#Konstructor
	def __init__(self, value):
		#do something
		self.value = value		#self acts like "this"

	def printSth(self):
		print("value of this instance is: ", self.value)


random = extended_val(5)
random.printSth()