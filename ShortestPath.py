#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:33:22 2021

@author: student
"""

import math
import time

class diGraph():
    
    def __init__(self, vertices, edges, costs):
        self.vertices = vertices    # list of vertices
        self.edges = edges          # list of tuples of directed edges
        self.costs = costs      # list of directed edge weights
        
    def solve_Fords_Algorithm(self, r):
        # Instantiate y,p dictionaries        
        y = {}
        p = {}
        
        # Instantiate y,p values
        for v in self.vertices:
            if v == r:
                y[v] = 0
                p[v] = 0
            else:
                y[v] = math.inf
                p[v] = -1
        
        # Fords Algorithm Using feasible potential as stopping criteria
        feasible_potential = False
        
        begin = time.time()   # record start time before algorithm execution
        
        # Algorithm for Ford's Algorithm. If algorithm runs for more than 10 seconds, we will break out of loop.
        while (feasible_potential == False):
            
            end = time.time()   # record current end time.
            
            if end - begin > 10:   # check time since beginning algorithm
                break
            
            # counter will keep track of how many y's satisfy feasible_potential property
            counter = 0
            
            for i in range(len(self.edges)):     # get current edge in graph
                
                e = self.edges[i]
                c = self.costs[i]
                
                if y[e[0]] + c < y[e[1]]:        # check for feasible potential
                    y[e[1]] = y[e[0]] + c
                    p[e[1]] = e[0]
                    i = 0
                    break;
                    
                else:
                    counter += 1
            
            # Assign true to feasible_potential if all y's satisfied feasible potential property
            if counter == len(self.edges):
                feasible_potential = True         # Break out of while loop
        
        # Print out distance (from source) and parent for each vertex if run time less than 10 seconds
        if end - begin < 10:
            print("The following are the y,p pairs for each vertex.")
            for v in self.vertices:
                print(v,":",(y[v],p[v]))
        else:
            print('Fords algorithm has entered infinite loop.')
                
        return y, p
    
    def solve_BellmanFords_Algorithm(self, r):
        # Instantiate y,p dictionaries        
        y = {}
        p = {}
        
        # Instantiate y,p values
        for v in self.vertices:
            if v == r:
                y[v] = 0
                p[v] = 0
            else:
                y[v] = math.inf
                p[v] = -1
        
        # Bellman Fords Algorithm 
        
        i = 1
        V = self.vertices
        E = self.edges
        C = self.costs
       
        # Iterate through all the edges |V| - 1 times
        while (i < len(V)):
        
            for j in range(len(E)):
                e = E[j]
                c = C[j]
                        
                if y[e[0]] + c < y[e[1]]:          # check for feasible potential
                    y[e[1]] = y[e[0]] + c
                    p[e[1]] = e[0]
              
            i=i+1
        
        # Get the distance and parent dictionaries
        y_1 = y.copy()
        p_1 = p.copy()
        
        # Check all the edges one more time to see if updated. If yes, the graph has a negative cycle.
        for j in range(len(E)):
            e = E[j]
            c = C[j]
                        
            if y[e[0]] + c < y[e[1]]:
                y[e[1]] = y[e[0]] + c
                p[e[1]] = e[0]
        
        # Get the distance and parent dictionaries.         
        y_2 = y.copy()
        p_2 = p.copy()
        
        # Compare the distance and parent dictaionries from the two loops. If NOT equal, we have negative cycle.
        if (y_1 == y_2) and (p_1 == p_2):
            print("The following are the y,p pairs for each vertex.")
            for v in self.vertices:
                print(v,":",(y[v],p[v]))
        else:
            print('Bellman Ford Algorithm has detected a negative cycle in the graph.')
            
        return y, p
    
    def solve_Dijkstras_Algorithm(self, r):
        S = self.vertices.copy()
        E = self.edges
        C = self.costs
        
        # Instantiate y,p dictionaries        
        y = {}
        p = {}
        
        # Instantiate y,p values
        for v in self.vertices:
            if v == r:
                y[v] = 0
                p[v] = 0
            else:
                y[v] = math.inf
                p[v] = -1
                
        y_copy = y.copy()
        
        # Dijkstra's Algorithm
        while (S != []):    
            yv_min_vertex = min(y_copy.keys(), key=(lambda k: y[k]))
            
            for i in range(len(E)):
                e = E[i]
                c = C[i]
                
                if e[0] == yv_min_vertex:
                    if y[e[0]] + c < y[e[1]]:
                        y[e[1]] = y[e[0]] + c
                        y_copy[e[1]] = y_copy[e[0]] + c
                        p[e[1]] = e[0]
              
            S.remove(yv_min_vertex)
            del y_copy[yv_min_vertex]
        
        # Output to User
        print("The following are the y,p pairs for each vertex.")
        for v in self.vertices:
            print(v,":",(y[v],p[v]))
        return y, p
            
            
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    # HW Instance
    V = ['r', 'a', 'b', 'p', 'q']
    E = [ ('r','a'), ('r','b'), ('a','b'), ('a','p'), ('b','q'), ('p','b'), ('p','q'), ('q','a'),]
    C = [2, 4, 3, 1, 2, 2, 4, 3]
    
    diGraph_int = diGraph(V, E, C)
    y1, p1 = diGraph_int.solve_Fords_Algorithm('r')
    y2, p2 = diGraph_int.solve_BellmanFords_Algorithm('r')
    y3, p3 = diGraph_int.solve_Dijkstras_Algorithm('r')
    
    
    
    
    
                
        
                

