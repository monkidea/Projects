#!/usr/bin/env python3

"""
Library file for the project to create
a Graph and find impossible Eulerian Cycle.
"""

class Vertex:

    def __init__(self, vertex_name):
        self.vertex_name = vertex_name
        self.adj_list = list()

class Graph:

    ImpossibleEulerCycleResult = ""

    def __init__(self, no_of_vertices):
        # Simple initialization function.
        self.no_of_vertices = no_of_vertices
        # Making array of vertices the size of the inputted no of vertices.
        self.vertices = [(Vertex("")) for i in range(no_of_vertices)]
        # Making an empty adjacency list for each vertex in the graph.
        for i in range(no_of_vertices):
            self.vertices[i].adj_list = list()
        # Represents the counter variable that will tell us the index of the current edge that's being added.
        self.counter = 0

    def add_vertex(self, vertex, *adjacent_vertices):
        """ Function to add a vertex.
            User will input vertex and the adjacent vertices.
            For example :
                  graph.add_vertex("A", "B", "C", "D", "E")
            This would imply that "A" is the vertex and "B", "C", "D" & "E" are the connected vertices.
        """
        # First, we check to make sure we haven't reached the max no of vertices.
        if(self.counter > self.no_of_vertices - 1):
            print("Reached maximum number of vertices, cannot add vertex {} and adjacency list {}".format(vertex, list(adjacent_vertices)))
            return 1   # Returning control here so that the next section doesn't execute.
        # Then we make sure that the user has inputted the adjacent vertices.
        elif(adjacent_vertices is None):
            print("Invalid Vertex, vertex must be connected to other vertices.")
            return 1    # Returning control here so that the next section doesn't execute.
        self.vertices[self.counter].vertex_name = vertex    # Adding vertex to current counter index.
        for i in range(len(adjacent_vertices)):
            # Adding all the adjacent vertices to the adjacency list of the current vertex.
            self.vertices[self.counter].adj_list.append(adjacent_vertices[i])
        self.counter += 1 # Increasing counter index.

    def isConnected(self, vertex_index, vertex_to_check):
        # Simple function to check if vertex in arg1 is connected to vertex in arg2.
        if(vertex_to_check not in self.vertices[int(vertex_index)].adj_list):
            return False
        else:
            return True

    def getVertexIndex(self, vertex_string):
        # Simple function that returns the index of vertex.
        for i in range(self.no_of_vertices):
            if(str(vertex_string) == str(self.vertices[i].vertex_name)):
                return i
            else:
                pass

    def traverse_to_vertex(vertex):
        # Simple function to add traversed vertex to final result.
        Graph.ImpossibleEulerCycleResult += str(vertex)+"->"

    def ImpossibleEulerCycle(self):
        """Main function that does all the work.
           The algorithm for this function is
           written in the writeup."""
        cntr = 1    # Counter variable
        current_vertex_index = 0    # Current vertex index
        start_node = self.vertices[current_vertex_index].vertex_name
        Graph.traverse_to_vertex(start_node)    # Adding start node to Result
        while(cntr < self.no_of_vertices):
            if((cntr == current_vertex_index) and (cntr != self.no_of_vertices-1)):
                cntr += 1   # Preventing self-traversal
            next_vertex = self.vertices[cntr].vertex_name
            if(Graph.isConnected(self, Graph.getVertexIndex(self, start_node), next_vertex)):
                # Travelling to and from next_vertex twice to ensure impossible cycle.
                Graph.traverse_to_vertex(next_vertex)
                Graph.traverse_to_vertex(start_node)
            else:
                for vertex in self.vertices[current_vertex_index].adj_list:
                    Graph.traverse_to_vertex(vertex)
                    if(Graph.isConnected(self, Graph.getVertexIndex(self, vertex), next_vertex)):
                        Graph.traverse_to_vertex(next_vertex)
                        Graph.traverse_to_vertex(vertex)
                        break
                    else:
                        Graph.traverse_to_vertex(start_node)
                Graph.traverse_to_vertex(start_node)
            if((cntr == self.no_of_vertices - 1) and (current_vertex_index != self.no_of_vertices - 1)):
                current_vertex_index += 1
                start_node = self.vertices[current_vertex_index].vertex_name
                cntr = 0
            else:
                cntr += 1

        # Now adding code to return to start node.                
        if(Graph.isConnected(self, Graph.getVertexIndex(self, start_node), self.vertices[0].vertex_name)):
            Graph.traverse_to_vertex(self.vertices[0].vertex_name)
        else:
            for vertex in self.vertices[current_vertex_index].adj_list:
                Graph.traverse_to_vertex(vertex)
                if(Graph.isConnected(self, Graph.getVertexIndex(self, vertex), self.vertices[0].vertex_name)):
                    Graph.traverse_to_vertex(self.vertices[0].vertex_name)
                    break
                else:
                    Graph.traverse_to_vertex(start_node)
                    
        print("Impossible Euler Cycle is :\n{}".format(Graph.ImpossibleEulerCycleResult[:-2]))
