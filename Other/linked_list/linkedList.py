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

  def insertBefore(self, el_add, el_pre):
    c = Node(self.search(el_pre))
    if (c == None):
      return
    if (c == self.start):
      self.insertBeg(el_add)
      return
    b = Node(el_add)
    a = c.prev
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b

  def deleteBeg(self):
    if (self.start == None):
      return None
    if (self.start == self.end):
      x = self.start
      self.start = None
      self.end = None
      return x
    y = self.start
    self.start = self.start.next
    self.start.prev = None
    return y

  def deleteEnd(self):
    if (self.start == None):
      return None
    if (self.start == self.end):
      x = self.start
      self.start = None
      self.end = None
      return x
    y = self.end
    self.end = self.end.prev
    self.end.next = None
    return y

  def del_search(self, x):
    a = Node(self.search(x))
    if (a == None):
      return None
    if (a == self.start):
      y = self.deleteBeg()
      return y
    if (a == self.end):
      z = Node(self.deleteEnd())
      return z
    a.prev.next = a.next
    a.next.prev = a.prev
    return a

  def print(self):
    temp = self.start
    while(temp != None):
      print(temp.data)
      temp = temp.next