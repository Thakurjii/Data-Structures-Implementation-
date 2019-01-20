"""   Binary Search Tree implementation   """


class Node(object):
    """   Represents a Node of Tree   """
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree(object):
    """   Represents a Binary Search Tree   """
    def __init__(self):
        self.root = None

    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)

    # private method to insert new element in B.S.T.
    def _insert_node(self, node, data):
        if node.data > data:
            if node.left_child is not None:
                self._insert_node(node.left_child, data)
            else:
                node.left_child = Node(data)
        else:
            if node.data < data:
                if node.right_child is not None:
                    self._insert_node(node.right_child, data)
                else:
                    node.right_child = Node(data)
    
    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def get_min_value(self):
        if self.root.data is not None:
            return self._get_min(self.root)
        else:
            return None
    
    # private method to get Minimum value from the B.S.T.
    def _get_min(self, node):
        if node.left_child is not None:
            return self._get_min(node.left_child)

        return node.data

    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def get_max_value(self):
        if self.root is not None:
            return self._get_max(self.root)
        else:
            return None
    
    # private method to get Minimum value from the B.S.T.
    def _get_max(self,node):
        if node.right_child is not None:
            return self._get_max(node.right_child)

        return node.data
    
    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def traverse_inorder(self):
        if self.root is not None:
            self._inorder(self.root)
        else:
            pass
    
    # private method for inorder traversal of B.S.T.
    def _inorder(self, node):
        if node.left_child is not None:
            self._inorder(node.left_child)
        print(node.data, end = ' ')
        if node.right_child is not None:
            self._inorder(node.right_child)
    
    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def traverse_preorder(self):
        if self.root is not None:
            self._preorder(self.root)
        else:
            pass
    
    # private method for preorder traversal of B.S.T.
    def _preorder(self, node):
        print(node.data, end = ' ')
        if node.left_child is not None:
            self._preorder(node.left_child)
        if node.right_child is not None:
            self._preorder(node.right_child)
    
    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def traverse_postorder(self):
        if self.root is not None:
            self._postorder(self.root)
        else:
            pass

    # private method for postorder traversal of B.S.T.
    def _postorder(self, node):
        if node.left_child is not None:
            self._postorder(node.left_child)
        if node.right_child is not None:
            self._postorder(node.right_child)
        print(node.data, end = ' ')
    
    # O(logN) Average time Complexity, O(n) Worst time Complexity
    def delete(self, data):
        if self.root is not None:
            self.root = self._remove(self.root, data)
    
    # private method for removing data from B.S.T
    def _remove(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left_child = self._remove(node.left_child, data)
        elif data > node.data:
            node.right_child = self._remove(node.right_child, data)
        else:
            if not node.left_child and not node.right_child:
                print('Deleting the leaf Node...')
                del node
                return None
            if not node.left_child:
                print('Deleting the Node with Right child...')
                temp_node = node.right_child
                del node.right_child
                return temp_node
            elif not node.right_child:
                print('Deleting the Node with Left chid...')
                temp_node = node.left_child
                del node.left_child
                return temp_node

            print('Deleting the Node with Both left and right Children...')
            temp_node = self._get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self._remove(node.left_child, temp_node.data)

        return node

    # private method to get the predecessor of any node.
    def _get_predecessor(self, node):
        if node.right_child:
            return self._get_predecessor(node.right_child)
        
        return node

if __name__ == '__main__':

    tree = Tree()

    tree.insert(7)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(10)
    tree.insert(11)
    tree.insert(9)
    tree.insert(2)
    
    print('Max value :',tree.get_max_value())
    print('Min value :',tree.get_min_value())
    print('Inorder Traversal : ', end = '')
    tree.traverse_inorder()
    print()
    print('Preorder Traversal : ', end = '')
    tree.traverse_preorder()
    print()
    print('Postorder Traversal : ', end = '')
    tree.traverse_postorder()
    print()
    tree.delete(4)
    tree.delete(3)
    print('Inorder Traversal : ', end = '')
    tree.traverse_inorder()