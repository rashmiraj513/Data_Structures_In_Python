# A Node class to represent each element in the linked list
class Node:
  # Constructor to initialize a node with data and next pointer
  def __init__(self, data, next=None):
    self.data = data
    self.next = next