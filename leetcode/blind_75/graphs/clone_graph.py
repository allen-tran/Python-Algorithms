class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
def cloneGraph(self, node):
    oldToNew = {}
        
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        
        tmp = Node(node.val)
        oldToNew[node] = tmp
        for nei in node.neighbors:
            tmp.neighbors.append(dfs(nei))
        return tmp
    
    return dfs(node) if node else None