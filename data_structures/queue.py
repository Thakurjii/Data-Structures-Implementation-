"""   Queue implementation from list   """


class Queue(object):
    """   Represents a Queue   """
    def __init__(self):
        self.queue = []

    # returns True if the Queue is empty
    def is_empty(self):
        return self.queue == []

    # inserts an element in the queue
    def enqueue(self, data):
        self.queue.append(data)

    # removes and returns the first added element from the queue
    def dequeue(self):
        first_element = self.queue[0]
        del self.queue[0]
        return first_element
    
    # returns the first added element of the queue
    def peek(self):
        return self.queue[0]
    
    # returns the size of the queue
    def get_size(self):
        return len(self.queue)
    

if __name__ == '__main__':
    queue1 = Queue()
    print('Queue is empty :', queue1.is_empty())
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    print('Queue is empty :', queue1.is_empty())
    print('Size :',queue1.get_size())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.peek())
    print('Queue is empty :', queue1.is_empty())
