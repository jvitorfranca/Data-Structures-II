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

		self.__array[key] = value.getVal(), value.getItem()

	def invertedIndex(self, words):
		keyLists = list(words.keys())
		keyLists.sort(key=lambda x: x[:ut.C])

		for word in keyLists:
			position = self.__keys[word]
			value = self.__array[position]
			print(value.getItem())

	def getArray(self):
		return self.__array

	def hash(self, data, iteration):
		int_value = 0

		for i in range(0, len(data)):
			int_value += ord(data[i])
			i += 1		

		return int(int_value/len(data) + iteration) % self.__size


heshi = HashTable(10)

heshi.insert("arroz", 1)
heshi.insert("feijao", 2)
heshi.insert("salada", 1)
heshi.insert("frango", 2)
heshi.insert("sobremesa", 1)

print(heshi.getArray())



