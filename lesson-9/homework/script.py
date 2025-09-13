import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
from datetime import datetime
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")
    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

p = Person("Ali", "Uzbekistan", "2000-05-10")
print("Age:", p.age())
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()
print("Add:", calc.add(5, 3))
print("Divide:", calc.divide(10, 2))
class Calculator:
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

calc = Calculator()
print("Yig‘indi:", calc.add(3, 5))
print("Ayirma:", calc.minus(10, 4))
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            if val < self.root.val:
                self.root.left = Node(val)
            else:
                self.root.right = Node(val)

t = BST()
t.insert(10)
t.insert(5)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()
s = Stack()
s.push(10)
s.push(20)
print(s.pop())
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def show(self):
        t = self.head
        while t:
            print(t.val, end=" -> ")
            t = t.next
        print("None")

l = LinkedList()
l.add(5)
l.add(10)
l.show()
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append(price)

    def total(self):
        return sum(self.items)

c = Cart()
c.add("Olma", 2000)
c.add("Banan", 3000)
print("Jami narx:", c.total())
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def show(self):
        print(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.show()
s.pop()
s.show()
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        return self.q.pop(0)

q = Queue()
q.enqueue(5)
q.enqueue(10)
print(q.dequeue())
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, x):
        self.balance += x

    def withdraw(self, x):
        if x <= self.balance:
            self.balance -= x

b = Bank("Ali", 1000)
b.deposit(500)
b.withdraw(300)
print("Qolgan pul:", b.balance)
