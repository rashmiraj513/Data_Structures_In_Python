# A Node class to represent each element in the linked list
class Node:
  # Constructor to initialize a node with data and next pointer
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# A Queue class using linked list
class Queue():
  # Constructor to initialize an empty queue with a front, rear node and a count of elements
  def __init__(self):
    self.front = None
    self.rear = None
    self.count = 0

  # Method to push a value onto the queue
  def push(self, value):
    # Create a new node with the given value
    new_node = Node(value)
    # Check if the queue is empty
    if not self.rear:
      # If empty, set front and rear node to `new_node`
      self.front = self.rear = new_node
    else:
      # If not empty, set rear's next pointer to new_node and update the rear pointer.
      self.rear.next = new_node
      self.rear = self.rear.next
    # Increment the count of elements in the queue
    self.count += 1

  # Method to pop the front value from the queue
  def pop(self):
    # Check if the queue is not empty
    if not self.empty():
      # Move the front pointer to the next node (effectively removing the front node)
      self.front = self.front.next
      # Decrement the count of elements in the queue
      self.count -= 1
    else:
      # Otherwise, print a statement saying `Queue is empty!`
      print('Queue is empty!')

  # Method to return the front element of the queue without removing it
  def first(self):
    # Check if the queue is not empty
    if not self.empty():
      # Return the data of the front node without removing it
      return self.front.data
    else:
      # Otherwise, print a message saying `Queue is empty!` and return None
      print('Queue is empty!')
      return None
    
  # Method to return the rear element of the queue without removing it
  def last(self):
    # Check if the queue is not empty
    if not self.empty():
      # Return the data of the rear node without removing it
      return self.rear.data
    else:
      # Otherwise, print a message saying `Queue is empty!` and return None
      print('Queue is empty!')
      return None
  
  # Method to check if the queue is empty
  def empty(self):
    # Return True if the front is None, indicating an empty queue
    return self.front is None
  
  # Method to display the elements of the queue
  def display(self):
    # Iterate through the linked list and print each element
    print('The Queue elements are: ', end="")
    curr = self.front
    while curr is not None:
      print(curr.data, end=" -> ")
      curr = curr.next
    print('NULL')
  
  # Method to get the size (count of elements) of the queue
  def size(self):
    return self.count
  
# Driver Code
if __name__ == '__main__':
  # Create an instance of the Queue class
  my_queue = Queue()

  # Enqueue elements into the queue
  my_queue.push(2)
  my_queue.push(3)
  my_queue.push(4)

  # Display the current elements in the queue
  my_queue.display()

  # Get the front element of the queue
  print('Front Element: ', my_queue.first())

  # Get the front element of the queue
  print('Rear Element: ', my_queue.last())

  # Dequeue an element from the queue
  my_queue.pop()
  my_queue.pop()

  # Display the updated elements in the queue
  my_queue.display()

  # Check if the queue is empty
  print("Is the queue empty: ", my_queue.empty())