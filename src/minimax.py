from cmath import inf


def minimax(node, depth, maximising):
    if(depth == 0 or len(node.children) == 0):
        return node.value
    if maximising:
        value = -inf
        for child in node.children:
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        value = inf
        for child in node.children:
            value = max(value, minimax(child, depth - 1, True))
        return value

def depthsearch(node, depth):
    if(depth == 0 or len(node.children) == 0):
        return node.value
    value = -inf
    
    for child in node.children:
        value = max(value, depthsearch(child, depth-1))
    return value