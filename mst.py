#################################################################################################
#   Name: Samy Masadi                                                                           #
#   Date: 26 Apr 2019                                                                           #
#   CSCI 423                                                                                    #
#                                                                                               #
#   The program finds minimum spanning trees using implementations of Kruskal's and Prim's      #
#   algorithms. It is meant to compare each method's resulting MST and their performance times. #
#################################################################################################

#################################################################################################
#   The following code was sourced from geekforgeeks.org and contributed by Neelam Yadav        #
#   and Divyanshu Mehta.                                                                        #
#   The code has been modified by Samy Masadi to suit the program requirements.                 #
#   https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/       #
#   https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/    #
#################################################################################################

from collections import defaultdict 
import sys

#Class to represent a graph
# The following functions have been modified to work with both Yadav's (for Kruskal)
# and Mehta's (for Prim) version of the Graph class.
class Graph: 
        def __init__(self,vertices): 
                self.V = vertices               #No. of vertices 
                self.edges = []                 # default dictionary to store graph edges (Kruskal's)
                self.graph = defaultdict(list)  # for adjancency list (Prim's)

        # function to add an edge to graph 
        def addEdge(self,src,dest,weight): 
                self.edges.append([src,dest,weight])    # Kruskal's just uses edges as they are

                # Add an edge from src to dest.  A new node is 
                # added to the adjacency list of src. The node  
                # is added at the begining. The first element of 
                # the node has the destination and the second  
                # elements has the weight 
                newNode = [dest, weight]
                self.graph[src].insert(0, newNode)      # Prim's uses the graph as an adj list.
                # Since graph is undirected, add an edge from  
                # dest to src also 
                newNode = [src, weight]
                self.graph[dest].insert(0, newNode)

#################################################################################################
#   The following code was sourced from geekforgeeks.org and contributed by Neelam Yadav.       #
#   The code has been modified by Samy Masadi to suit the program requirements.                 #
#   https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/       #
#################################################################################################

        # A utility function to find set of an element i 
        # (uses path compression technique) 
        def find(self, parent, i): 
                if parent[i] == i: 
                        return i 
                return self.find(parent, parent[i]) 

        # A function that does union of two sets of x and y 
        # (uses union by rank) 
        def union(self, parent, rank, x, y): 
                xroot = self.find(parent, x) 
                yroot = self.find(parent, y) 

                # Attach smaller rank tree under root of 
                # high rank tree (Union by Rank) 
                if rank[xroot] < rank[yroot]: 
                        parent[xroot] = yroot 
                elif rank[xroot] > rank[yroot]: 
                        parent[yroot] = xroot 

                # If ranks are same, then make one as root 
                # and increment its rank by one 
                else : 
                        parent[yroot] = xroot 
                        rank[xroot] += 1

        # The main function to construct MST using Kruskal's algorithm 
        def KruskalMST(self): 

                result =[] #This will store the resultant MST 

                i = 0 # An index variable, used for sorted edges 
                e = 0 # An index variable, used for result[] 

                        # Step 1: Sort all the edges in non-decreasing 
                        # order of their 
                        # weight. If we are not allowed to change the 
                        # given graph, we can create a copy of graph 
                self.edges = sorted(self.edges,key=lambda item: item[2]) 

                parent = [] ; rank = [] 

                # Create V subsets with single elements 
                for node in range(self.V): 
                        parent.append(node) 
                        rank.append(0) 
        
                # Number of edges to be taken is equal to V-1 
                while e < self.V -1 : 

                        # Step 2: Pick the smallest edge and increment 
                        # the index for next iteration 
                        u,v,w = self.edges[i] 
                        i = i + 1
                        x = self.find(parent, u) 
                        y = self.find(parent ,v) 

                        # If including this edge does't cause cycle, 
                        # include it in result and increment the index 
                        # of result for next edge 
                        if x != y: 
                                e = e + 1       
                                result.append([u,v,w]) 
                                self.union(parent, rank, x, y)                   
                        # Else discard the edge 

                # print the contents of result[] to display the built MST 
                #print ("Following are the edges in the constructed MST")
                for u,v,weight in result: 
                        #print str(u) + " -- " + str(v) + " == " + str(weight) 
                        print ("%d -- %d == %d" % (u+1,v+1,weight)) 

#################################################################################################
#   The following code was sourced from geekforgeeks.org and contributed by Divyanshu Mehta.    #
#   The code has been modified by Samy Masadi to suit the program requirements.                 #
#   https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/    #
#################################################################################################

        def PrimMST(self):
                # Get the number of vertices in graph
                V = self.V
                
                # key values used to pick minimum weight edge in cut 
                key = []
                
                # List to store contructed MST 
                parent = []  
          
                # minHeap represents set E 
                minHeap = Heap() 
          
                # Initialize min heap with all vertices. Key values of all 
                # vertices (except the 0th vertex) is is initially infinite 
                for v in range(V): 
                    parent.append(-1) 
                    key.append(sys.maxsize) 
                    minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
                    minHeap.pos.append(v) 
          
                # Make key value of 0th vertex as 0 so  
                # that it is extracted first 
                minHeap.pos[0] = 0
                key[0] = 0
                minHeap.decreaseKey(0, key[0]) 
          
                # Initially size of min heap is equal to V 
                minHeap.size = V; 
          
                # In the following loop, min heap contains all nodes 
                # not yet added in the MST. 
                while minHeap.isEmpty() == False: 
          
                    # Extract the vertex with minimum distance value 
                    newHeapNode = minHeap.extractMin() 
                    u = newHeapNode[0]
                    # Modification: Print edges as nodes are chosen from the min heap (greedy choice)
                    if u > 0:
                            print(parent[u]+1, "--", u+1, "==", newHeapNode[1])
          
                    # Traverse through all adjacent vertices of u  
                    # (the extracted vertex) and update their  
                    # distance values 
                    for pCrawl in self.graph[u]: 
          
                        v = pCrawl[0] 
          
                        # If shortest distance to v is not finalized  
                        # yet, and distance to v through u is less than 
                        # its previously calculated distance 
                        if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
                            key[v] = pCrawl[1]
                            parent[v] = u
          
                            # update distance value in min heap also 
                            minHeap.decreaseKey(v, key[v]) 

                # Modification: Unnecessary to print MST at the end.
                # Program prints edges and weights as they are chosen instead.
                #printArr(parent, V)
  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes of  
    # min heap. Needed for min heapify 
    def swapMinHeapNode(self, a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped. Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2 * idx + 1
        right = 2 * idx + 2
  
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min heap  
        # if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is not  
        # hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)//2 ) 
  
            # move to parent index 
            i = (i - 1) // 2; 
  
    # A utility function to check if a given vertex 
    # 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
# Modification: Function is not used in this program, but is included for completeness
#def printArr(parent, n): 
#    for i in range(1, n): 
#        print ("% d - % d" % (parent[i]+1, i+1)) 

#################################################################################################
#       Main Program                                                                            #
#################################################################################################
import time     # for performance measurement

# Construct city circuit graph by adding each edge
# Edge represented as (start node, end node, edge weight)
cityCircuit = Graph(10)
cityCircuit.addEdge(0, 1, 32)
cityCircuit.addEdge(0, 3, 17)
cityCircuit.addEdge(1, 4, 45)
cityCircuit.addEdge(2, 3, 18)
cityCircuit.addEdge(2, 6, 5)
cityCircuit.addEdge(3, 4, 10)
cityCircuit.addEdge(3, 7, 3)
cityCircuit.addEdge(4, 5, 28)
cityCircuit.addEdge(4, 8, 25)
cityCircuit.addEdge(5, 9, 6)
cityCircuit.addEdge(6, 7, 59)
cityCircuit.addEdge(7, 8, 4)
cityCircuit.addEdge(8, 9, 12)

# Find MSTs using each method and print results
print("Kruskal's MST in the order edges were chosen:")
start = time.perf_counter()
cityCircuit.KruskalMST()
end = time.perf_counter()
print("\nTime taken:", end-start, "seconds")
print("\nPrim's MST in the order edges were chosen:")
start = time.perf_counter()
cityCircuit.PrimMST()
end = time.perf_counter()
print("\nTime taken:", end-start, "seconds")
