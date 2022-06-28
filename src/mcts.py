from cmath import inf
import cmath
import random

# Evaluate UCB1 for specific node
def evaluate(node):
    if(node.visits == 0):
        return inf
    return node.value/node.visits + 1.41 * cmath.sqrt(cmath.log(node.parent.visits)/node.visits)

# Find best child node
def selectUCB1(node):
    if(len(node.children) == 0):
        return node
    max_value = -inf
    selected_child = None
    for child in node.children:
        curr_value = evaluate(child)
        if(curr_value > max_value):
            max_value = curr_value
            selected_child = child
    return selected_child

# Find best child node
def selectValue(node):
    if(len(node.children) == 0):
        return node
    max_value = -inf
    selected_child = None
    for child in node.children:
        if(child.visits == 0):
            curr_value = 0
        else:
            curr_value = child.value/child.visits + 1.41 * cmath.sqrt(cmath.log(node.visits)/child.visits)
        if(curr_value > max_value):
            max_value = curr_value
            selected_child = child
    return selected_child

# Find best leaf node
def expand(node):
    if(len(node.children) == 0):
        return node
    return expand(selectUCB1(node))

# Play rest of the game at random
def rollout(node):
    gameover = node.get_gameover()
    if(gameover is True):
        return (node, node.value)
    
    return rollout(random.choice(list(node.generate_states()))) # WARNING: choice from set deprecated, list from set O(n) time

def rollout_avg(node, nb_rollouts):
    for i in range(nb_rollouts):
        leaf, reward = rollout(node)
        backpropagate(leaf, reward)
    return 

# Update visited nodes with reward 
def backpropagate(node, value):
    while(node.parent is not None):
        node.value += value
        node = node.parent
    return node

def findMove(node):
    max_iter = 1000
    i = 0
    input()
    while(i < max_iter):
        curr_node = selectUCB1(node)
        curr_node = expand(curr_node)
        #rollout_avg(curr_node, 100)
        curr_node, reward = rollout(curr_node)
        backpropagate(curr_node, reward)
        print(curr_node.id)

        i += 1
        
    return selectValue(node)