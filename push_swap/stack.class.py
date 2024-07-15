from collections import deque

class Stack:
	def __init__(self):
		self.numbers = deque()

	def rot(self):
		self.numbers.rotate(1)

	def rev_rot(self):
		self.numbers.rotate(-1)

	def swap(self):
		self.numbers[0], self.numbers[1] = self.numbers[1], self.numbers[0]

	def pop(self):
		tmp = self.numbers[0]
		self.numbers.popleft()
		return tmp

	def push(self, num):
		self.numbers.insert(0, num)
