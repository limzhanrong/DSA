from collections import deque
class Solution:
    # BFS with a stack, 
    # before going to the next while loop, 
    # append all children onto stack from the left most side to the right most side.
    # Iterates through the length of the stack. and popleft() on every iteration.
    def rightSideView(self, root):
        if not root:
            return root
        output = []
        q = deque([root])
        print(q)
        while q:
            qLength = len(q)
            mostRightNode = None
            for i in range(qLength):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    mostRightNode = node
            if mostRightNode:
                output.append(mostRightNode.val)
        return output