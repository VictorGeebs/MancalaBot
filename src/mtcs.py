from cmath import inf
import cmath
import random

class Node:
    def __init__(self, state=None):
        self.state = state
        self.children = set()
        self.parent = None
        self.visits = 0
        self.value = 0

# TODO implement
def evaluate(node):
    if(node.visits == 0):
        return inf
    return node.value/node.visits + 1.41 * cmath.sqrt(cmath.log(node.parent.visits)/node.visits)

# Find best child node
def selection(node):
    max_value = -inf
    selected_child = None
    for child in node.children:
        curr_value = evaluate(child)
        if(curr_value > max_value):
            max_value = curr_value
            selected_child = child
    return selected_child

# Find best leaf node
def expansion(node):
    if(node.children.empty()):
        return node
    return expansion(selection(node))

# Play rest of the game at random
def rollout(node):
    gameover = node.get_gameover()
    if(gameover is True):
        return (node, node.value)
    
    return rollout(random.choice(node.generate_states))

# Update visited nodes with reward 
def backpropagate(node, value):
    while(node.parent is not None):
        node.value += value
        node = node.parent
    return node
