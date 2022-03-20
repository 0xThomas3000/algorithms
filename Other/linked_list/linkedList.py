from .node import Node

class LinkedList:
  def __init__(self):
    self.start = None
    self.end = None

  def insertBeg(self, data):
    newNode = Node(data)
    if (self.start == None):
      self.start = newNode
      self.end = newNode
      return
    self.start.prev = newNode
    newNode.next = self.start
    self.start = newNode

  def insertEnd(self, x):
    newNode = Node(x)
    if (self.start == None):
      self.start = newNode
      self.end = newNode
      return
    self.end.next = newNode
    newNode.prev = self.end
    self.end = self.end.next

  def insertAfter(self, el_add, el_pre):
    a = Node(self.search(el_pre))
    if (a == None):
      return
    if (a == self.end):
      self.insertEnd(el_add)
      return
    b = Node(el_add)
    c = a.next
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b