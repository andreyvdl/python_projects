from stack import Stack
from collections import deque


class PushSwap:
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()
        self.sorted = Stack()
        self.moves = int()

    def __str__(self):
        return (f"Total moves: {self.moves}\nStack A:[{self.stack_a}]\n"
                f"Stack B:[{self.stack_b}]")

    def __iter__(self):
        for n in self.stack_a.numbers:
            yield n

    def ready(self):
        self.sorted.numbers = deque(sorted(self.stack_a.numbers))

    def add_number(self, num):
        self.stack_a.add(num)

    def is_sorted(self):
        return self.stack_a.numbers == deque(sorted(self.stack_a.numbers))

    def rot_a(self):
        if len(self.stack_a) < 2:
            return
        self.stack_a.rot()
        self.moves += 1
        print("ra")

    def rot_b(self):
        if len(self.stack_b) < 2:
            return
        self.stack_b.rot()
        self.moves += 1
        print("rb")

    def rot_rot(self):
        if len(self.stack_a) < 2 or len(self.stack_b) < 2:
            return
        self.stack_a.rot()
        self.stack_b.rot()
        self.moves += 1
        print("rr")

    def rev_rot_a(self):
        if len(self.stack_a) < 2:
            return
        self.stack_a.rev_rot()
        self.moves += 1
        print("rra")

    def rev_rot_b(self):
        if len(self.stack_b) < 2:
            return
        self.stack_b.rev_rot()
        self.moves += 1
        print("rrb")

    def rev_rot_rot(self):
        if len(self.stack_a) < 2 or len(self.stack_b) < 2:
            return
        self.stack_a.rev_rot()
        self.stack_b.rev_rot()
        self.moves += 1
        print("rrr")

    def swap_a(self):
        if len(self.stack_a) < 2:
            return
        self.stack_a.swap()
        self.moves += 1
        print("sa")

    def swap_b(self):
        if len(self.stack_b) < 2:
            return
        self.stack_b.swap()
        self.moves += 1
        print("sb")

    def swap_swap(self):
        if len(self.stack_a) < 2 or len(self.stack_b) < 2:
            return
        self.stack_a.swap()
        self.stack_b.swap()
        self.moves += 1
        print("ss")

    def push_a(self):
        if len(self.stack_b) == 0:
            return
        num = self.stack_b.pop()
        self.stack_a.push(num)
        self.moves += 1
        print("pa")

    def push_b(self):
        if len(self.stack_a) == 0:
            return
        num = self.stack_a.pop()
        self.stack_b.push(num)
        self.moves += 1
        print("pb")
