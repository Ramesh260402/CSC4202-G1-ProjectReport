# CSC4202-G1-Project


## 1. Introduction: (1 min) (ramesh)
#very Brief overview of the university course scheduling problem scenario.
#brief model development


## 2. Problem Description: 

a. Time conflicts
b. Prerequisite dependencies
c. Course availability (capacity)
d. Credit constraints 
e. Student preferences

Focus: b, c & d

## 3. Algorithm Selection: 
  1. Sorting 
- Strengths: Sorting can be useful for certain aspects of the course scheduling problem, such as ordering the courses based on prerequisites or sorting them by certain criteria like course credits or semester availability.
- Weaknesses: Sorting alone cannot handle the full complexity of the course scheduling problem, as it doesn't consider prerequisites or credit constraints. 


 2. Divide and Conquer (DAC)
- Strengths: DAC could be used to break down the course scheduling problem into smaller subproblems, solving each subproblem independently, and then combining the solutions. This approach can be effective when dealing with complex dependency structures.
- Weaknesses: DAC may not directly address the prerequisites or credit constraints, and additional steps would be needed to ensure the overall schedule satisfies the requirements. 


 3. Dynamic Programming (DP)
- Strengths: DP can be useful when there are overlapping subproblems and optimal substructure properties. It could potentially handle the course scheduling problem by considering the dependencies and credits, building a schedule incrementally, and finding an optimal solution.
- Weaknesses: DP might be challenging to handle real-time updates or changes to the schedule.


 4. Greedy Algorithms
- Strengths: Greedy algorithms can provide simple and efficient solutions by making locally optimal choices at each step. In the course scheduling problem, a greedy approach could involve selecting the courses based on certain criteria, such as the number of prerequisites or credits.
- Weaknesses: Greedy algorithms may not always guarantee an optimal global solution, especially when considering complex constraints like prerequisites and credit limits. The locally optimal choices made by the greedy algorithm may lead to suboptimal or infeasible schedules.


 5.  Graph Algorithms
- Strengths: Graph algorithms, such as topological sorting or shortest path algorithms, can directly address the dependencies and prerequisites in the course scheduling problem. They provide a natural representation for modeling the relationships between courses and can help in building a schedule that satisfies the constraints.
- Weaknesses: Graph algorithms may not inherently consider credit constraints, and additional steps would be required to incorporate them into the scheduling process. They may also require careful consideration of edge cases and exceptional scenarios to ensure the correctness and efficiency of the schedule.

Hence, we agree to choose the graph algorithms, specifically topological sorting, as the solution paradigm for our Course Scheduling problem. Topological sorting is well-suited for this problem because it effectively handles prerequisites and credit constraints.




## 4. Topological Sorting 
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

Time Complexity

1. Creating the graph: The code iterates over the course input and prerequisites, adding nodes and edges to the graph. This step takes O(|V| + |E|) time, where |V| is the number of courses and |E| is the number of prerequisites.

2. Topological sorting: The topological sorting algorithm used is Kahn's algorithm, which has a time complexity of O(|V| + |E|). It involves calculating in-degrees, enqueuing nodes with in-degree 0, and processing nodes in the queue to update in-degrees and generate the sorted order.

3. Creating the schedule: The code iterates over the sorted nodes and performs various operations based on the course data and constraints. In the worst case, it may iterate over all the courses and perform checks for each prerequisite and semester. Thus, the time complexity is dependent on the number of courses and their attributes.

In summary, the algorithm has a time complexity of O(|V| + |E|), where |V| is the number of courses and |E| is the number of prerequisites. It correctly creates the course graph, performs topological sorting, and generates a valid course schedule considering prerequisites, desired credits, and the starting semester.

## 8. Conclusion 
-The optimization of university course scheduling is a crucial task that requires careful consideration of various factors 

-Manual scheduling processes are prone to errors 

-Graph algorithms, specifically topological sorting, provide a suitable solution paradigm for the course scheduling problem

-Topological sorting ensures a valid order for course scheduling
