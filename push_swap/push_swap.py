from stack import Stack

class PushSwap:
	def __init__(self):
		self.stack_a = Stack()
		self.stack_b = Stack()

	def __str__(self):
		return str(self.stack_a.numbers) + "\n" + str(self.stack_b.numbers)

	def rot_a(self):
		if len(self.stack_a) < 2:
			return
		self.stack_a.rot()

	def rot_b(self):
		if len(self.stack_b) < 2:
			return
		self.stack_b.rot()

	def rot_rot(self):
		if len(self.stack_a) < 2 or len(self.stack_b) < 2:
			return
		self.rot_a()
		self.rot_b()

	def rev_rot_a(self):
		if len(self.stack_a) < 2:
			return
		self.stack_a.rev_rot()

	def rev_rot_b(self):
		if len(self.stack_b) < 2:
			return
		self.stack_b.rev_rot()

	def rev_rot_rot(self):
		if len(self.stack_a) < 2 or len(self.stack_b) < 2:
			return
		self.rev_rot_a()
		self.rev_rot_b()

	def swap_a(self):
		if len(self.stack_a) < 2:
			return
		self.stack_a.swap()

	def swap_b(self):
		if len(self.stack_b) < 2:
			return
		self.stack_b.swap()

	def swap_swap(self):
		if len(self.stack_a) < 2 or len(self.stack_b) < 2:
			return
		self.stack_a.swap()
		self.stack_b.swap()

	def push_a(self):
		if len(self.stack_b) == 0:
			return
		num = self.stack_b.pop()
		self.stack_a.push(num)

	def push_b(self):
		if len(self.stack_a) == 0:
			return
		num = self.stack_a.pop()
		self.stack_b.push(num)
