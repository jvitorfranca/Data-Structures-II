import utilities as ut
import word as wd
import random
import math

# Represents the elements: id_file; occurencies
class HashElm:
	def __init__(self, key, item):
		self.key = key
		self.item = item

	def getItem(self):
		return self.item

	def getVal(self):
		return self.key

# The table itself
class HashTable:
	def __init__(self, size):
		if size <= 0:
			size = 10
		self.__size = size
		self.__keys = {}
		self.__array = [0 for x in range(self.__size)]

	def __getitem__(self, key):
		if key not in self.__keys:
			return None
		position = self.__keys[key]
		elm = self.__array[position]
		if elm is not None:
			return elm.getVal()
		return None

	def getKeys(self):
		return self.__keys

	def getArray(self):
		return self.__array

	def insert(self, data, item, option):
		i = 0

		# Defining wether option the user choose
		if option == 'linear':

			key = self.hash(data, i, 'linear')

			while self.__array[key] != 0:
				i += 1
				key = self.hash(data, i, 'linear')

		elif option == 'quadratic':

			key = self.hash(data, i, 'quadratic')

			while self.__array[key] != 0:
				i += 1
				key = self.hash(data, i, 'quadratic')

		# Creating a element based on the input and putting it into the array
		value = HashElm(data, item)
		
		self.__array[key] = value

	def invertedIndex(self, words):
		keyLists = list(words.keys())
		keyLists.sort(key=lambda x: x[:ut.C])

		for word in keyLists:
			position = self.__keys[word]
			value = self.__array[position]
			print(value.getVal())

	def hash(self, data, iteration, option):
		int_value = 0

		word = data.getVal()
		lenght = data.getValueLenght()

		for i in range(0, lenght):
			int_value += ord(word[i])
			i += 1

		A = (math.sqrt(5) - 1)/2

		k = int(int_value/lenght)

		if option == 'linear':

			# Division method
			h = (k + iteration) % self.__size

			# Multiplication method
			# h = math.floor(self.__size*(((k + iteration)*A)%1))

		elif option == 'quadratic':

			# Division method
			h = (k + iteration**2) % self.__size

			# Multiplication method
			# h = math.floor(self.__size*(((k + iteration**2)*A)%1))

		self.__keys[word] = h

		return h