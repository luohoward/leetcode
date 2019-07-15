# does not completely pass. Tried timing self. Passes 39/42

def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    classes = {}
    
    for i in range(numCourses):
        classes[i] = []
        
    for depClass, prereq in prerequisites:
        classes[prereq].append(depClass)
        
    for key, value in classes.items():
        seen = set()
        queue = []
        
        for v in value:
            queue.append((key, v))

        while len(queue) != 0:
            preceding, currentNode = queue.pop()

            if (preceding, currentNode) in seen:
                return False

            else:
                seen.add((preceding, currentNode))
                
                for neighbor in classes[currentNode]:
                    queue.insert(0, (currentNode, neighbor))
                    
    return True