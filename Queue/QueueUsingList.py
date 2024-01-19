# A Queue class
class Queue:
  # Constructor to initialize an empty list to store the queue elements
  def __init__(self):
    self.arr = []

  # Method to push a value into the queue (enqueue)
  def push(self, value):
    self.arr.append(value)

  # Method to pop the front element from the queue (dequeue)
  def pop(self):
    # Check if the queue is not empty before dequeuing
    if not self.empty():
      self.arr.pop(0)
    else:
      # If the queue is empty, print a statement saying `Queue is empty!`
      print('Queue is empty!')

  # Method to get the front element of the queue without removing it
  def front(self):
    # Check if the queue is not empty before returning the front element
    if not self.empty():
      return self.arr[0]
    else:
      # If the queue is empty, print a statement saying `Queue is empty!` and return None
      print('Queue is empty!')
      return None

  # Method to get the rear element of the queue without removing it
  def rear(self):
    # Check if the queue is not empty before returning the rear element
    if not self.empty():
      return self.arr[self.size() - 1]
    else:
      # If the queue is empty, print a statement saying `Queue is empty!` and return None
      print('Queue is empty!')
      return None

  # Method to check if the queue is empty
  def empty(self):
    # Use len() to get the size of the queue and check if it's 0
    return len(self.arr) == 0

  # Method to display the elements of the queue
  def display(self):
    print('The Queue elements are: ', self.arr)

  # Method to get the size of the queue
  def size(self):
    return len(self.arr)

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
  print('Front Element: ', my_queue.front())

  # Get the front element of the queue
  print('Rear Element: ', my_queue.rear())

  # Dequeue an element from the queue
  my_queue.pop()
  my_queue.pop()
  my_queue.pop()

  # Display the updated elements in the queue
  my_queue.display()

  # Check if the queue is empty
  print("Is the queue empty: ", my_queue.empty())