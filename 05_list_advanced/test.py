lab = [[1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,0,0,1],[1,0,1,1,1,1,1,1,0,1,1,1],[1,0,1,0,0,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,1,1,0,1],[1,0,1,0,1,0,0,0,0,0,0,1],[1,0,0,0,1,1,0,1,1,1,0,1],[1,0,1,0,0,0,0,1,0,1,1,1],[1,0,1,1,0,1,0,0,0,0,0,1],[1,0,1,0,0,1,1,1,1,1,0,1],[1,0,0,0,1,1,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1]]

class Node:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.neighbours = [ (x + xoff, y + yoff) for xoff, yoff in
            ( (1, 0), (0, 1), (0, -1), (-1, 0) )
            if not lab [y + yoff] [x + xoff] ]
        self.distance = ...
        self.path = ...
        self.visited = False

    def __repr__ (self):
        return '{}: ({})'.format ( (self.x, self.y), self.neighbours)

nodes = {}
for y in range (12):
    for x in range (12):
        if lab [y] [x]: continue
        nodes [x, y] = Node (x, y)

current = nodes [1, 1]
current.distance = 0
current.path = []
unvisited = set (nodes.keys () )

while True:
    dist = current.distance + 1
    for nx, ny in current.neighbours:
        if (nx, ny) not in unvisited: continue
        neighbour = nodes [nx, ny]
        if neighbour.distance is ... or neighbour.distance > dist:
            neighbour.distance = dist
            neighbour.path = current.path + [ (current.x, current.y) ]
    current.visited = True
    unvisited.remove ( (current.x, current.y) )
    if not unvisited: break
    current = sorted ( [node for node in nodes.values ()
        if not node.visited and node.distance is not ...],
        key = lambda node: node.distance) [0]

print (nodes [10, 10].path)
path = nodes [10, 10].path + [ (10, 10) ]
for (ax, ay), (bx, by) in zip (path, path [1:] ):
    if ax == bx and ay > by: print ('N', end = '')
    if ax == bx and ay < by: print ('S', end = '')
    if ay == by and ax > bx: print ('W', end = '')
    if ay == by and ax < bx: print ('E', end = '')
print ()