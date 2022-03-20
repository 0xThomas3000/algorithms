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