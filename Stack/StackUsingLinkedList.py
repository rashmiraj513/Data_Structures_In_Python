# A Node class to represent each element in the linked list
class Node:
  # Constructor to initialize a node with data and next pointer
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# A Stack class using linked list
class Stack:
  # Constructor to initialize an empty stack with a top node and a count of elements
  def __init__(self):
    self.top = None
    self.count = 0

  # Method to push a value onto the stack
  def push(self, value):
    # Check if the stack is empty
    if not self.top:
      # If empty, create a new node with the given value
      self.top = Node(value)
    else:
      # If not empty, create a new node, set its next pointer to the current top,
      # and update the top to the new node
      new_node = Node(value, next=self.top)
      self.top = new_node
    # Increment the count of elements in the stack
    self.count += 1

  # Method to pop the top element from the stack
  def pop(self):
    # Check if the stack is not empty
    if not self.empty():
      # Move the top pointer to the next node (effectively removing the top node)
      self.top = self.top.next
      # Decrement the count of elements in the stack
      self.count -= 1
    else:
      # Otherwise print a statement saying `Stack is empty!`
      print('Stack is empty!')

  # Method to return the top element of the stack without removing it
  def peek(self):
    # Check if the stack is not empty
    if not self.empty():
      # Return the data of the top node without removing it
      return self.top.data
    else:
      # Otherwise print a statement saying `Stack is empty!` and return None
      print('Stack is empty!')
      return None

  # Method to check if the stack is empty
  def empty(self):
    # Return True if the top is None, indicating an empty stack
    return self.top is None

  # Method to display the elements of the stack
  def display(self):
    # Iterate through the linked list and print each element
    print('The Stack elements are: ', end='')
    curr = self.top
    while curr is not None:
      print(curr.data, end=' -> ')
      curr = curr.next
    print('NULL')

  # Method to get the size (count of elements) of the stack
  def size(self):
    return self.count

# Driver Code
if __name__ == '__main__':
  # Create a new stack
  my_stack = Stack()

  # Push elements onto the stack
  my_stack.push(2)
  my_stack.push(3)
  my_stack.push(4)

  # Display the current stack elements
  my_stack.display()

  # Print the top element of the stack
  print('Top Element: ', my_stack.peek())

  # Pop the element from the stack
  my_stack.pop()
  # my_stack.pop()
  # my_stack.pop()

  # Display the current stack elements
  my_stack.display()

  # Whether the stack is empty or not
  print('Is the stack empty: ', my_stack.empty())