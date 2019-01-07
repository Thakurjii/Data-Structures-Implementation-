"""   LinkedList Implementation   """

class Node(object):
	"""   Represents a Single Node of LinkedList   """
	def __init__(self, data):
		self.data = data
		self.next_node = None


class LinkedList(object):
	"""   Represents a LinkedList   """
	def __init__(self):
		self.head = None
		self.size = 0

	# O(1)
	def insert_at_start(self, data):
		new_node = Node(data)
		self.size = self.size + 1
		if self.head == None:
			self.head = new_node
		else:
			new_node.next_node = self.head
			self.head = new_node

	# O(n)
	def insert_at_last(self, data):
		new_node = Node(data)
		self.size = self.size + 1
		if self.head == None:
			self.head = new_node
		else:
			current_node = self.head
			while current_node.next_node is not None:
				current_node = current_node.next_node
			current_node.next_node = new_node

	# O(n)
	def traverse(self):
		current_node = self.head
		for i in range(self.size):
			print(current_node.data)
			current_node = current_node.next_node

	# O(1)
	def get_size(self):
		return self.size

	# O(n)
	def remove_element(self, data):
		current_node = self.head
		if current_node.data == data:
			self.head = current_node.next_node
			self.size = self.size - 1
		else:
			previous_node = None
			while current_node.data != data:
				previous_node = current_node
				current_node = current_node.next_node
			previous_node.next_node = current_node.next_node
			self.size = self.size - 1

if __name__ == '__main__':
	list1 = LinkedList()
	list1.insert_at_start(2)
	list1.insert_at_start(1)
	list1.insert_at_last(3)
	print('Size is', str(list1.get_size()))
	list1.traverse()
	list1.remove_element(3)
	print('Size is', str(list1.get_size()))
	list1.traverse()
	list1.remove_element(2)
	print('Size is', str(list1.get_size()))
	list1.traverse()
	list1.remove_element(1)
	print('Size is', str(list1.get_size()))
	list1.traverse()
