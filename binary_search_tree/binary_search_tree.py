"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if new is < node.value
        if value < self.value:
            # No left..end
            if self.left is None:
                # Create a left tree Node...
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        # Value is >= value
        else:
            # No right..end
            if self.right is None:
                # Create right tree
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
            #tree contains value
        if self.value == target:  
                return True #contains the value
        elif target < self.value: #if less go left/False
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:  #if more go right/False
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self 
        while current_node.right is not None: #if there is a value to the right
            current_node = current_node.right  #set to value to the right
        return current_node.value #return current value 
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)  #call function on value that we are on

        if self.left: #if not None
            self.left.for_each(fn)  #call the function on each
        
        if self.right: #if not None
            self.right.for_each(fn) #call function on each
    

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
