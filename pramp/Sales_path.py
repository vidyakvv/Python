""""
Sales Path

The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary).
The root is the company itself, and every node in the tree represents a car distributor that receives cars
from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars
direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

                            0
                     /      |     \
                  5         3       6
               /         /    \   /   \
             4          2     0  1    5
                      /      /
                     1      10
                      \
                      1


A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree,
is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path.
For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode,
write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

"""


def get_cheapest_path(root):
    stack = [(root, root.data)]
    min_path = float('inf')

    while stack:
        node, curr_cost = stack.pop()

        if not node.children:
            min_path = min(min_path, curr_cost)
        else:
            for child in node.children:
                stack.append((child, child.data + curr_cost))

    return min_path


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

        """
                  0
               /   |   \
              5    3    6
             /    /
            4    2
        """


root = Node(0)
five = Node(5)
three = Node(3)
six = Node(6)
four = Node(4)
two = Node(2)
root.children = [five, three, six]
five.children = [four]
three.parent = root
six.parent = root
five.parent = root
three.children = [two]
four.parent = five
two.parent = three

print(get_cheapest_cost(root))

