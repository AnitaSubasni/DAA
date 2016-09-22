
import random
import networkx as nx
import copy
import operator
import pylab

def algo_B(G,noOfNodes,active):

    rangeNodes = range(noOfNodes)
    colorOfNodes =[""]*noOfNodes
    flag = True

    while flag:
        flag = False
        # generate random bits for the number of nodes and compare with the neighbors
        r = random.getrandbits(noOfNodes)
        bits = list((format(r,'0'+str(noOfNodes)+'b')))
        print(bits)

        # comparing with neighbors iterating over active
        for i in rangeNodes:  # active is a list of size n
            # concatenate bits with color  string
            colorOfNodes[i] = colorOfNodes[i].__add__(bits[i])
            if(active[i]==[]):
                continue
            flag = True
            neighbors = copy.deepcopy(active[i])
            for j in neighbors:
                if bits[i]!=bits[j-1]:
                    active[i].remove(j)
    return colorOfNodes


############################ MAIN  ###########################
G=nx.Graph()
#noOfNodes = input("Enter the number of nodes : ")


print("Enter the edges separated by a , Eg: 1,2. Press 0 to stop :");

while True :
    edges = input()
    if edges == '0':
        break
    a = edges.split(sep = ',')
    G.add_edge(int(a[0]),int(a[1]))

noOfNodes = nx.number_of_nodes(G)
neighbors = []
for i in range(noOfNodes):
        neigh = nx.all_neighbors(G,i+1)
        neigh1 = []
        for ii in neigh:
            neigh1.append(ii)
        neighbors.append(neigh1)

maxDegree = len((max(neighbors,key=len)))
colors = algo_B(G,noOfNodes,copy.deepcopy(neighbors))
print(colors)


        # must form the di graph. iterate through the neighbors list and compare with the colors bits generated.
DG = nx.DiGraph()
inVertices = copy.deepcopy(neighbors)
outVertices = copy.deepcopy(neighbors)

for i in range(noOfNodes):
    for j in neighbors[i]:
        if(colors[i] < colors[j-1]):
            DG.add_edge(i+1,j)
          #  print(inVertices[i],j)
            inVertices[i].remove(j)
          #  print(outVertices[j],i)
            outVertices[j-1].remove(i+1)

print(DG.edges())
print(inVertices)
print(outVertices)
maxColors = maxDegree+1
colorOfNodes = [-1]*noOfNodes
#print(colorOfNodes)
r = list(range(maxColors))
colorPalette = []
for i in range(noOfNodes):
    colorPalette.append(list(r))


#print(colorPalette)

        # find the in and out degree of each node. sort it as max outDegree, min InDegree.
        # start with max-out degree with in degree -0
        # each time while coloring, get the colors from all the in-neighbours and remove them from the color palette.
        # give the smallest color to that node and proceed.
        # each time when a node is colored, make that degrees as [],just so the same node index is not
        # repeated each time. This is for duplicates

    # find the in and out degrees.
degrees = []
for i in range(noOfNodes):
    id = nx.DiGraph.in_degree(DG,i+1)
    od = nx.DiGraph.out_degree(DG,i+1)
    degrees.append([id,od])

sortedDegrees = copy.deepcopy(degrees)
degreesCopy = copy.deepcopy(degrees)
        # sort them in max-out, min-in format
sortedDegrees = sorted(sortedDegrees,key= operator.itemgetter(1),reverse=True)
sortedDegrees = sorted(sortedDegrees,key= operator.itemgetter(0))

    # start the coloring from smallest one
for i in range(noOfNodes):
    index = degrees.index(sortedDegrees[i])   # find which node actually has these degrees
        # get all the colors of inVertices.
    for j in inVertices[index]:
        col = colorOfNodes[j-1]
        if colorPalette[index].__contains__(col):
            colorPalette[index].remove(col)
    colorOfNodes[index] = colorPalette[index][0]
    degrees[index] = []    # this is to avoid retrieving the same node in cae of duplication
print(colorOfNodes)
