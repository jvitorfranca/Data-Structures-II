import utilities
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

	def insert(self, data):
		key = self.hash(data)

		while self.__array[key] != 0:
			key = self.hash(data + 1)

		self.__array[key] = data

	def getArray(self):
		return self.__array

	def hash(self, data):
		cont = 0
		for i in range(0, len(data)):
			cont += ord(data[i])
			i += 1		

		return int(cont/len(data)) % self.__size


heshi = HashTable(10)

heshi.insert("pao")
heshi.insert("queijo")
heshi.insert("presunto")

print(heshi.getArray())



