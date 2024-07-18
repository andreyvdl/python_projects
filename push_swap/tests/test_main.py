from inspect import currentframe, getframeinfo
from collections import deque
from push_swap import PushSwap
import random
import unittest


class testMoves(unittest.TestCase):
	def testPDF(self):
		# creating object
		ps = PushSwap()
		ps.stack_a.numbers.extend([2, 1, 3, 6, 5, 8])
		expected_a = deque([2, 1, 3, 6, 5, 8])
		expected_b = deque([])
		self.assertEqual(ps.stack_a.numbers, expected_a, "LINE " + str(getframeinfo(currentframe()).lineno))
		self.assertEqual(ps.stack_b.numbers, expected_b, "LINE " + str(getframeinfo(currentframe()).lineno))

		# swap first
		ps.swap_a()
		expected_a = deque([1, 2, 3, 6, 5, 8])
		self.assertEqual(ps.stack_a.numbers, expected_a, "LINE " + str(getframeinfo(currentframe()).lineno))
		self.assertEqual(ps.stack_b.numbers, expected_b, "LINE " + str(getframeinfo(currentframe()).lineno))

		# 3 pb
		ps.push_b()
		ps.push_b()
		ps.push_b()
		expected_a = deque([6, 5, 8])
		expected_b = deque([3, 2, 1])
		self.assertEqual(ps.stack_a.numbers, expected_a, "LINE " + str(getframeinfo(currentframe()).lineno))
		self.assertEqual(ps.stack_b.numbers, expected_b, "LINE " + str(getframeinfo(currentframe()).lineno))

		# ra + rb / rr
		# ps.rot_a()
		# ps.rot_b()
		ps.rot_rot()
		expected_a = deque([5, 8, 6])
		expected_b = deque([2, 1, 3])
		self.assertEqual(ps.stack_a.numbers, expected_a, "LINE " + str(getframeinfo(currentframe()).lineno))
		self.assertEqual(ps.stack_b.numbers, expected_b, "LINE " + str(getframeinfo(currentframe()).lineno))

		# rra + rrb / rrr
		# ps.rev_rot_a()
		# ps.rev_rot_b()
		ps.rev_rot_rot()
		expected_a = deque([6, 5, 8])
		expected_b = deque([3, 2, 1])
		self.assertEqual(ps.stack_a.numbers, expected_a, "LINE " + str(getframeinfo(currentframe()).lineno))
		self.assertEqual(ps.stack_b.numbers, expected_b, "LINE " + str(getframeinfo(currentframe()).lineno))

		# 3 pa
		ps.swap_a()
		ps.push_a()
		ps.push_a()
		ps.push_a() # does nothing
		expected_a = deque([1, 2, 3, 5, 6, 8])
		expected_b = deque([])
		self.assertEqual(ps.stack_a.numbers, expected_a, "LINE " + str(getframeinfo(currentframe()).lineno))
		self.assertEqual(ps.stack_b.numbers, expected_b, "LINE " + str(getframeinfo(currentframe()).lineno))


	def 


if __name__ == "__main__":
	unittest.main()
