from cmath import inf
import cmath
import math
import random

# Evaluate UCB1 for specific node
def evaluate(node):
    if(node.visits == 0):
        return inf
    return node.value/node.visits + 1.41 * math.sqrt(math.log(node.parent.visits)/node.visits)

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
            curr_value = child.value/child.visits + 1.41 * math.sqrt(math.log(node.visits)/child.visits)
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
    gameover = node.state.get_gameover()
    if(gameover is True):
        return node
    
    return rollout(random.choice(list(node.generate_states()))) # WARNING: choice from set deprecated, list from set O(n) time

def rollout_avg(node, n):
    gameover = node.state.get_gameover()
    if(gameover is True):
        return node
    
    return rollout(random.choice(list(node.generate_states())))

# Update visited nodes with reward 
def backpropagate(node, value):
    while(node.parent is not None):
        node.value += value
        node = node.parent
        node.visits += 1
    node.value += value
    node.visits += 1
    return node

def findMove(node):
    max_iter = 1000
    i = 0
    init_player = node.state.get_player()
    while(i < max_iter):
        curr_node = expand(node)
        curr_node = rollout(curr_node)
        reward = node.state.get_reward(init_player)
        curr_node.value = reward
        backpropagate(curr_node, reward)

        i += 1
        
    return selectValue(node)