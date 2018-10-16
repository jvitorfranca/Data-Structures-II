import utilities as ut
import word as wd
import random

class HashElm:
	def __init__(self, key, item):
		self.key = key
		self.item = item

	def getItem(self):
		return self.item

	def getVal(self):
		return self.key

class HashTable:
	def __init__(self, size):
		if size <= 0:
			size = 10
		self.__size = size
		self.__keys = {}
		self.__array = [0 for x in range(self.__size)]

	def insert(self, data, item):
		i = 0

		key = self.hash(data, i)

		while self.__array[key] != 0:
			i += 1
			key = self.hash(data, i)

		value = HashElm(data, item)

		self.__array[key] = value

	def getKeys(self):
		return self.__keys

	def invertedIndex(self, words):
		keyLists = list(words.keys())
		keyLists.sort(key=lambda x: x[:ut.C])

		for word in keyLists:
			position = self.__keys[word]
			value = self.__array[position]
			print(value.getVal())

	def getArray(self):
		return self.__array

	def hash(self, data, iteration):
		int_value = 0

		word = data.getVal()

		for i in range(0, data.getValueLenght()):
			int_value += ord(word[i])
			i += 1		

		h = int(int_value/data.getValueLenght() + iteration) % self.__size

		self.__keys[word] = h

		return h





