# CSC4202-G1-Project


## 1. Introduction: (1 min) (ramesh)
#very Brief overview of the university course scheduling problem scenario.
#brief model development


## 2. Problem Description:  (1 min) (syakila)

a. Time conflicts
b. Prerequisite dependencies
c. Course availability (capacity)
d. Credit constraints 
e. Student preferences

Focus: b, c & d

## 3. Algorithm Selection: (2 min) (qistina)
#Discuss the various solution paradigms, such as sorting, divide and conquer, dynamic programming, greedy algorithms, and graph algorithms. 
#justify why you chose the graph algorithm (topological sorting) as the suitable solution.

## 4. Topological Sorting (3 min) (ramesh)
![image](https://github.com/Ramesh260402/CSC4202-G1-ProjectReport/assets/86455045/7938d0dc-1f4e-407f-93c7-60114f7735bc)

## 5. Implementation Overview: (3 min) (mugi/ syakila)

def create_top_sort(self):
        # Perform topological sorting using Kahn's algorithm
        in_degree = {node: 0 for node in self.course_graph.nodes}
        queue = []

        # Calculate in-degree for each node
        for node in self.course_graph.nodes:
            for neighbor in self.course_graph.neighbors(node):
                in_degree[neighbor] += 1

        # Enqueue nodes with in-degree 0
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        # Perform topological sorting
        sorted_nodes = []
        while queue:
            node = queue.pop(0)
            sorted_nodes.append(node)

            for neighbor in self.course_graph.neighbors(node):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Create a new graph with sorted nodes and edges
        new_graph = nx.DiGraph()
        new_graph.add_nodes_from(sorted_nodes)
        new_graph.add_edges_from(self.course_graph.edges())

        # Copy node data from the original graph to the sorted graph
        nodes = new_graph.nodes
        nodes_old = self.course_graph.nodes
        for course in nodes:
            nodes[course]["data"] = nodes_old[course]["data"]

        self.top_graph = new_graph


ROLE OF TOPOLOGICAL SORTING IN COURSE SCHEDULING
1. Resolving dependencies
2. Establishing a feasible schedule
3. Handling cyclic dependencies
4. Generating a sorted graph


## 6. Code Demonstration: (1 min?) (mugi/ syakila)
#Present the code demonstration (video or real time??)
#also show how the java one works 
#Use visual aids, such as code snippets, diagrams, or slides, to enhance understanding. Keep the demonstration concise and focused on the key aspects of the algorithm.

## 7. Time complexity: (3) (qistina/ mugi)
#Time complexity of specific part of algorithm (important) python
#kalau sempat baru explain the java one
#Time complexity of whole system (just briefly)

## 8. Conclusion 
-The optimization of university course scheduling is a crucial task that requires careful consideration of various factors 

-Manual scheduling processes are prone to errors 

-Graph algorithms, specifically topological sorting, provide a suitable solution paradigm for the course scheduling problem

-Topological sorting ensures a valid order for course scheduling
