"""
Python data structures and algo practice 
"""


class Node:
    """
	Basic node object type

	left_node ==> memory pointer for binary tree example
	right_node ==> memory pointer for binary tree example
	next_node ==> memory pointer for queue / stack examples

	data ==> simple value (int)
	"""

    def __init__(self, data=None):
        self.data = data  # is data is passed asign it
        self.left_node = None
        self.right_node = None
        self.next_node = None


"""
Queue 

FIFO Linear data structure with flexible sizing  
"""

# asign H/T to null objects to make logic easier
head_node = None
# remove nodes here

tail_node = None

# add nodes here


def queue_is_empty():
    if head_node == None:
        return True
    else:
        return False


def queue_peek():
    if head_node == None:
        return "error msg: queue is empty"
    else:
        return head_node.data


def queue_add(data):
    global tail_node, head_node  # pull global vars into scope to update values

    new_node = Node(data)

    if (tail_node != None):
        tail_node.next_node = new_node  # point current tail's next at new_node

    tail_node = new_node  # set tail to point at new_node

    if (head_node == None):
        head_node = new_node


def queue_remove():
    global head_node, tail_node  # pull global vars into scope to update values

    data = head_node.data
    head_node = head_node.next_node
    if (head_node == None):
        tail_node = None

    return data

"""
Stack FIFO data structure with flexible sizing 
"""

top_node = None # global var for stack 

def stack_is_empty():
	pass


def stack_peek():
	pass


def stack_push():
	pass


def stack_pop():
	pass


##################################

def queue_run():
    test_node = Node(24)
    print("Test node is a ", test_node.__class__)
    print("\nLet's use these nodes to make a queue...\n")

    print("Is queue empty? ", queue_is_empty())
    print(queue_peek())

    print("\nOk. Now lets add a few nodes... 2, 34, 53, 6")
    queue_add(2)
    queue_add(34)
    queue_add(53)
    queue_add(6)
    print("Now if we run remove on our queue we get ==> " +
          str(queue_remove()))
    print("\nThen running it again we get...")
    print("==> " + str(queue_remove()))
    print("==> " + str(queue_remove()))
    print("==> " + str(queue_remove()))
    print("\nNow is the queue empty? ", queue_is_empty())


def stack_run():
	pass

def binary_search_tree_run():
    """
	Binary search tree 

	create tree using ordered insert and lookup to get log N memory/time space 

	value on left child is less than parent and right child is more
	binary search trees must be balanced to avoid losing log n time 

	"""

    # no need for Tree object as the Tree itself is a concept; its made of connected nodes
    # nodes are the object; connections are self contained

    def binary_insert(root, node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.l_child is None:
                    root.l_child = node
                else:
                    binary_insert(root.l_child, node)
            else:
                if root.r_child is None:
                    root.r_child = node
                else:
                    binary_insert(root.r_child, node)

    def in_order_print(root):
        if not root:
            return
        in_order_print(root.l_child)
        print(root.data)
        in_order_print(root.r_child)


#################################

def main():
    queue_run()
	stack_run()
    binary_search_tree_run()

if (__name__ == "__main__"):
    main()
