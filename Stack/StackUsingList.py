# A Stack class
class Stack:
  # Constructor to initialize an empty list to store the stack elements
  def __init__(self):
    self.arr = []

  # Method to push a value onto the stack
  def push(self, value):
    self.arr.append(value)

  # Method to pop the top element from the stack
  def pop(self):
    # If the stack is not empty then only pop an element from the stack
    if not self.empty():
      self.arr.pop()
    else:
      # Otherwise print a statement saying `Stack is empty!`
      print("Stack is empty!")

  # Method to peek at the top element of the stack without removing it
  def peek(self):
    # If the stack is not empty then only return the top element
    if not self.empty():
      return self.arr[-1]
    else:
      # Otherwise print a statement saying `Stack is empty!`
      print("Stack is empty!")
      return None

  # Method to check if the stack is empty
  def empty(self):
    # Use len() to get the size of the stack and check if it's 0
    return len(self.arr) == 0

  # Method to display the elements of the stack
  def display(self):
    # Simply print the entire stack
    print('The Stack elements are: ', self.arr)

  # Method to calculate the size of the stack
  def size(self):
    # Use len() to get the size of the stack and return it
    return len(self.arr)


# Driver Code
if __name__ == "__main__":
  # Create a new stack
  my_stack = Stack()

  # Push elements onto the stack
  my_stack.push(2)
  my_stack.push(3)
  my_stack.push(4)

  # Display the current stack elements
  my_stack.display()

  # Print the top element of the stack
  print("Top Element: ", my_stack.peek())

  # Pop the element from the stack
  my_stack.pop()
  my_stack.pop()
  my_stack.pop()

  # Display the current stack elements
  my_stack.display()

  # Whether the stack is empty or not
  print("Is the stack empty: ", my_stack.empty())
