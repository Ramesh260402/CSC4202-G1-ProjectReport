# CSC4202-G1-ProjectReport

1.0 Original Scenario

Optimization of University Course Scheduling

Scenario: Timetabling issues can occur in a range of industries, such as healthcare, sports, transportation, and education. Here, we concentrate
on a particular subset of scheduling issues known as the university course scheduling issue. This issue is frequently experienced in a lot of
colleges around the world. Teacher assignment, course scheduling, class-teacher timetabling, student scheduling, and classroom
assignment are the five sub-problems that it can be further divided into.

The scheduling of students is the topic of this project. Imagine you are a student at university who has to come up with the optimal course
schedule or best course plan for the forthcoming semester. The institution offers a wide range of courses with various start times,
requirements, and seat capacity.

The number of desirable courses should be maximized while avoiding timing conflicts and fulfilling prerequisite requirements. An organized
schedule ought to guarantee an equal distribution of professor and student groups. The planning of the class schedule is a crucial and challenging undertaking. 
Because there are so many courses, manual scheduling ultimately results in conflicts of various types, and its flaws
become more obvious. The drawbacks of manual scheduling will be remedied by computer scheduling as computer science and technology
advance. 



2.0 Importance of Optimal Solution

Finding an optimal solution for the university course scheduling scenario is important for several reasons:

1. Maximizing Course Availability: An optimal course schedule allows students to enroll in a maximum number of desirable courses. By efficiently organizing the course offerings, students have a better chance of obtaining the courses they need or want to take, leading to a more fulfilling educational experience.

2. Avoiding Timing Conflicts: Scheduling conflicts can arise when two or more courses that a student wishes to take are offered at the same time. By optimizing the course schedule, conflicts can be minimized, providing students with more flexibility in selecting their courses and reducing the need for time-consuming adjustments or compromises.

3. Fulfilling Prerequisite Requirements: Some courses have prerequisite requirements, meaning students must complete certain courses before being eligible to enroll in higher-level courses. An optimal course schedule takes these prerequisites into account and ensures that students can fulfill the necessary requirements in a logical and efficient manner.

4. Efficient Resource Allocation: Optimizing the course schedule allows for the efficient allocation of resources such as classrooms, professors, and teaching assistants. By evenly distributing these resources across different courses and time slots, the institution can make the most effective use of available resources and avoid potential bottlenecks or inefficiencies.

5. Improved Student and Professor Satisfaction: A well-organized course schedule reduces stress and frustration for both students and professors. Students can plan their semester more effectively, ensuring a balanced workload and minimizing conflicts between courses. Professors benefit from a better distribution of student groups, allowing for more manageable class sizes and facilitating effective teaching and interaction.

6. Time and Cost Savings: Manual scheduling can be a time-consuming and error-prone process, especially when dealing with a large number of courses, students, and constraints. By automating the scheduling process and finding an optimal solution, significant time and effort can be saved for students, professors, and administrative staff. This, in turn, can lead to cost savings for the institution.

In summary, finding an optimal course schedule in the university course scheduling scenario is important for maximizing course availability, avoiding conflicts, fulfilling prerequisites, efficient resource allocation, improving satisfaction, and achieving time and cost savings. By leveraging computer scheduling and optimization techniques, the drawbacks of manual scheduling can be addressed, leading to a more effective and streamlined scheduling process.



3.0 Suitability of Algorithms As Solution Paradigm

Let's review the suitability of different solution paradigms for the course scheduling problem, considering sorting, Divide and Conquer (DAC), Dynamic Programming (DP), greedy algorithms, and graph algorithms.

3.1 Sorting
   - Strengths: Sorting can be useful for certain aspects of the course scheduling problem, such as ordering the courses based on prerequisites or sorting them by certain criteria like course credits or semester availability.
   - Weaknesses: Sorting alone cannot handle the full complexity of the course scheduling problem, as it doesn't consider prerequisites or credit constraints. It may require additional algorithms or techniques to ensure that the sorted schedule satisfies the constraints.

3.2 Divide and Conquer (DAC)
   - Strengths: DAC could be used to break down the course scheduling problem into smaller subproblems, solving each subproblem independently, and then combining the solutions. This approach can be effective when dealing with complex dependency structures.
   - Weaknesses: DAC may not directly address the prerequisites or credit constraints, and additional steps would be needed to ensure the overall schedule satisfies the requirements. Handling the combination of solutions and maintaining consistency across subproblems can also be challenging.

3.3 Dynamic Programming (DP)
   - Strengths: DP can be useful when there are overlapping subproblems and optimal substructure properties. It could potentially handle the course scheduling problem by considering the dependencies and credits, building a schedule incrementally, and finding an optimal solution.
   - Weaknesses: DP can be computationally expensive for large input sizes, and it may require defining an appropriate state and recursive relationship that captures the course dependencies and credit constraints. It can also be challenging to handle real-time updates or changes to the schedule.

3.4 Greedy Algorithms
   - Strengths: Greedy algorithms can provide simple and efficient solutions by making locally optimal choices at each step. In the course scheduling problem, a greedy approach could involve selecting the courses based on certain criteria, such as the number of prerequisites or credits.
   - Weaknesses: Greedy algorithms may not always guarantee an optimal global solution, especially when considering complex constraints like prerequisites and credit limits. The locally optimal choices made by the greedy algorithm may lead to suboptimal or infeasible schedules.

3.5 Graph Algorithms
   - Strengths: Graph algorithms, such as topological sorting or shortest path algorithms, can directly address the dependencies and prerequisites in the course scheduling problem. They provide a natural representation for modeling the relationships between courses and can help in building a schedule that satisfies the constraints.
   - Weaknesses: Graph algorithms may not inherently consider credit constraints, and additional steps would be required to incorporate them into the scheduling process. They may also require careful consideration of edge cases and exceptional scenarios to ensure the correctness and efficiency of the schedule.

In summary, a combination of approaches may be suitable for the course scheduling problem. Graph algorithms, such as topological sorting, can handle the prerequisites and dependencies, while other techniques like sorting, DAC, DP, or greedy algorithms can be employed to address additional constraints or optimize the scheduling process. The choice of approach would depend on the specific requirements, complexity of the problem, available input data, and performance considerations.



3.6 Final Choice of Algorithm 

We decided to choose the graph algorithms which is topologically sorting to implement our scenario. This is because

Graph algorithms, particularly topological sorting, are well-suited for solving the Course Scheduling problem that involves considering prerequisites and credit constraints. Here are the reasons why topological sorting is a suitable solution paradigm for this problem:

1. Prerequisite dependencies: The Course Scheduling problem inherently involves prerequisites, where certain courses must be completed before taking others. Graph algorithms, such as topological sorting, are designed to handle dependencies between nodes in a graph. By representing the courses and prerequisites as nodes and edges in a directed graph, topological sorting can efficiently determine the order in which the courses should be taken.

2. Credit constraints: In addition to prerequisites, credit constraints are an essential consideration when creating a course schedule. Topological sorting does not directly address credit constraints, but it provides the foundation for incorporating such constraints into the scheduling algorithm. After obtaining the topological order, additional checks and algorithms can be implemented to assign courses to specific semesters while considering credit limits.

3. Efficiency: Topological sorting has a time complexity of O(|V| + |E|), where |V| represents the number of courses and |E| represents the number of prerequisites. This time complexity is generally efficient for the Course Scheduling problem, especially considering that the number of prerequisites and courses is typically manageable. By utilizing topological sorting, the algorithm can generate a valid course schedule in a reasonable amount of time.

4. Correctness: Topological sorting guarantees that the courses are scheduled in a valid order, satisfying all prerequisites. It ensures that no course is taken before its prerequisites are completed, thus maintaining the correctness of the schedule. By relying on a well-established algorithm, the Course Scheduling solution can provide accurate and reliable results.

5. Scalability: Graph algorithms, including topological sorting, are scalable and can handle larger instances of the Course Scheduling problem. As long as the number of courses and prerequisites remains within a reasonable range, topological sorting can efficiently generate the course schedule without significant performance issues.

In summary, topological sorting is a suitable solution paradigm for the Course Scheduling problem due to its ability to handle prerequisite dependencies, potential integration with credit constraints, efficiency, correctness, and scalability. By utilizing this graph algorithm, you can generate a valid course schedule while considering prerequisites and credit constraints efficiently.


3.7 Consideration

3.7.1 Implementing Dynamic Programming

However one consideration when we are completing this project is to implement Dynamic Programming for Course Scheduling Problem in the subset of Class Capacity Problem 

Dynamic programming can be a suitable solution paradigm for the Classroom Selection problem. Here's a review of its suitability:

1. Optimal substructure: Dynamic programming is effective when a problem can be divided into overlapping subproblems, and the optimal solution can be constructed from the optimal solutions of its subproblems. In the Classroom Selection problem, the goal is to find the class with the minimum excess capacity, which can be seen as finding the optimal solution by considering the capacities of individual classes. Thus, the problem exhibits optimal substructure, making dynamic programming a viable approach.

2. Overlapping subproblems: The dynamic programming approach in the code snippet utilizes a 2D table (dp) to store intermediate results. Each cell in the table represents the minimum number of classrooms required to accommodate a certain number of students for a subset of classes. By filling in this table iteratively, the algorithm effectively solves overlapping subproblems and avoids redundant computations.

3. Time complexity: The time complexity of the dynamic programming solution is O(n * m), where n is the number of classes and m is the total number of students. The nested loops in the code iterate over the class capacities and the number of students, respectively. Since the dimensions of the table are proportional to the number of classes and the total number of students, the time complexity remains manageable even for larger problem instances.

4. Efficiency: Dynamic programming offers an efficient solution for the Classroom Selection problem. By computing and storing intermediate results in the dp table, the algorithm avoids redundant computations and optimizes the search for the class with the minimum excess capacity. The use of dynamic programming ensures that the solution is obtained in an efficient and systematic manner.

5. Correctness: The dynamic programming approach in the code snippet correctly determines the class with the minimum excess capacity. It computes the minimum number of classrooms required to accommodate different numbers of students for each subset of classes and identifies the class with the closest capacity to the total number of students.

In summary, dynamic programming is a suitable solution paradigm for the Classroom Selection problem. It leverages the problem's optimal substructure and overlapping subproblems to efficiently find the class with the minimum excess capacity. The approach ensures correctness, efficiency, and manageable time complexity, making it a viable solution strategy for this problem.


3.7.2 Sample of Implementation

This is the example of implementation
![image](https://github.com/Ramesh260402/CSC4202-G1-ProjectReport/assets/86455045/bcddb05d-75c4-4188-aa9f-e5b34ee07af9)

![image](https://github.com/Ramesh260402/CSC4202-G1-ProjectReport/assets/86455045/40f0e400-73e0-4e9c-a0ac-808667f97ee2)

4.0 Design The Algorithm

4.1 Topological Sorting 

4.1.1 Kahn's algorithm for topological sorting (Python)

1. Initialize the in-degree dictionary to store the in-degree of each node in the course_graph as 0.
2. Calculate the in-degree for each node by iterating over the nodes and their neighbors, incrementing the in-degree of each neighbor in the in_degree dictionary. This step does not require any recurrence.
3. Enqueue nodes with an in-degree of 0 into the queue by iterating over the nodes in the in_degree dictionary and adding the nodes with an in-degree of 0 to the queue. This step also does not require any recurrence.
4. Perform the topological sorting using Kahn's algorithm. This part does not involve recurrence.
-Initialize an empty list sorted_nodes to store the sorted nodes.
-While the queue is not empty, dequeue a node from the front of the queue.
-Append the dequeued node to the sorted_nodes list.
-Iterate over the neighbors of the dequeued node:
---Decrement their in-degree in the in_degree dictionary.
---If the in-degree of a neighbor becomes 0, enqueue it into the queue.
5. Create a new directed graph new_graph of type nx.DiGraph().
6. Add nodes to new_graph from the sorted_nodes list. This step does not require recurrence.
7. Add edges to new_graph by copying the edges from the original course_graph. This step does not require recurrence.
8. Copy node data from the original course_graph to the corresponding nodes in new_graph. This step does not require recurrence.
9. Assign new_graph to the self.top_graph variable.

    In summary, the algorithm uses an iterative approach and does not require any recurrence. The main idea is to calculate the in-degrees of nodes, enqueue nodes with an in-degree of 0, perform topological sorting using Kahn's algorithm, create a new graph with the sorted nodes and edges, and finally copy the node data from the original graph to the sorted graph. There is no specific optimization function mentioned in the given code.

4.1.2 Topological sorting using DFS (Java)

1. The CourseScheduler2 class is initialized with the number of courses (numCourses) and the prerequisites for each course (prerequisites).
2. The constructor initializes the necessary data structures and populates the prerequisites list with the prerequisite courses for each course.
3. The canFinish() method is used to check if all the courses can be finished without any cyclic dependencies. This method calls the hasCycle() method for each course that has not been visited yet.
4. The hasCycle() method uses a recursive approach to check for cycles in the course dependencies. It marks the current course as visited and adds it to the recursionStack to keep track of the current path. It recursively checks the prerequisite courses and returns true if a cycle is detected.
5. The printCourseSchedule() method prints the course schedule if it is possible to schedule all the courses without cyclic dependencies. It retrieves the course names using the getCourseName() method and prints them in reverse order.
6. The getCourseName() method can be modified to map course IDs to their respective names according to a specific naming convention.

In terms of algorithm paradigm, the main part of the algorithm that involves recurrence is the hasCycle() method. It uses recursion to traverse the prerequisite courses and check for cycles. The recursion allows the algorithm to explore the dependencies in a depth-first manner.Regarding optimization, the algorithm could potentially benefit from memoization or caching techniques to avoid redundant calculations or lookups of course names. However, the given code does not incorporate any specific optimization function.Overall, the algorithm uses a recursive approach to detect cycles in course dependencies and determine if all courses can be scheduled without cyclic dependencies.

5.0 Algorithm Analysis

5.1 Topological Sorting 

5.1.1 Kahn's algorithm for topological sorting (Python)

The provided code implements a course scheduling algorithm using a directed graph representation and performs topological sorting to create a course schedule. Let's analyze the correctness and time complexity of the algorithm.

Correctness:
1. Creating the graph: The `create_graph` method constructs a directed graph based on the input course data. It iterates over each course and its prerequisites, adding nodes and edges to the graph accordingly. The course data is stored as attributes for each node. This step correctly represents the course dependencies in the graph.

2. Topological sorting: The `create_top_sort` method performs topological sorting on the course graph using Kahn's algorithm. It calculates the in-degree of each node, enqueues nodes with in-degree 0, and then performs the sorting by processing nodes in the queue. The resulting sorted nodes are used to create a new graph. This step correctly generates a valid order of courses to satisfy prerequisites.

3. Creating the schedule: The `create_schedule` method creates a course schedule based on the sorted graph. It iterates over the sorted nodes, considering the prerequisites and credits for each course. It assigns courses to semesters while taking into account the desired credits and the starting semester. The schedule is generated as a dictionary representing years and semesters. This step correctly schedules the courses based on the given constraints.

Overall, the algorithm correctly creates a course graph, performs topological sorting, and generates a valid course schedule considering prerequisites, desired credits, and starting semester.

Time Complexity:

1. Creating the graph: The code iterates over the course input and prerequisites, adding nodes and edges to the graph. This step takes O(|V| + |E|) time, where |V| is the number of courses and |E| is the number of prerequisites.

2. Topological sorting: The topological sorting algorithm used is Kahn's algorithm, which has a time complexity of O(|V| + |E|). It involves calculating in-degrees, enqueuing nodes with in-degree 0, and processing nodes in the queue to update in-degrees and generate the sorted order.

3. Creating the schedule: The code iterates over the sorted nodes and performs various operations based on the course data and constraints. In the worst case, it may iterate over all the courses and perform checks for each prerequisite and semester. Thus, the time complexity is dependent on the number of courses and their attributes.

Therefore, the overall time complexity of the algorithm is O(|V| + |E|), where |V| is the number of courses and |E| is the number of prerequisites.

Note: The space complexity of the algorithm is O(|V| + |E|) as it stores the course graph, topologically sorted graph, and the course schedule.

In summary, the algorithm has a time complexity of O(|V| + |E|), where |V| is the number of courses and |E| is the number of prerequisites. It correctly creates the course graph, performs topological sorting, and generates a valid course schedule considering prerequisites, desired credits, and the starting semester.

5.1.2 Topological sorting using DFS (Java)

The algorithm presented in the code solves the problem of determining whether a set of courses can be scheduled without any cyclic dependencies. Here's the breakdown of the algorithm design and the idea behind it:

1. The `CourseScheduler2` class is initialized with the number of courses (`numCourses`) and the prerequisites for each course (`prerequisites`).
2. The constructor initializes the necessary data structures and populates the `prerequisites` list with the prerequisite courses for each course.
3. The `canFinish()` method is used to check if all the courses can be finished without any cyclic dependencies. This method calls the `hasCycle()` method for each course that has not been visited yet.
4. The `hasCycle()` method uses a recursive approach to check for cycles in the course dependencies. It marks the current course as visited and adds it to the `recursionStack` to keep track of the current path. It recursively checks the prerequisite courses and returns true if a cycle is detected.
5. The `printCourseSchedule()` method prints the course schedule if it is possible to schedule all the courses without cyclic dependencies. It retrieves the course names using the `getCourseName()` method and prints them in reverse order.
6. The `getCourseName()` method can be modified to map course IDs to their respective names according to a specific naming convention.

In terms of algorithm paradigm, the main part of the algorithm that involves recurrence is the `hasCycle()` method. It uses recursion to traverse the prerequisite courses and check for cycles. The recursion allows the algorithm to explore the dependencies in a depth-first manner.

Regarding optimization, the algorithm could potentially benefit from memoization or caching techniques to avoid redundant calculations or lookups of course names. However, the given code does not incorporate any specific optimization function.

Overall, the algorithm uses a recursive approach to detect cycles in course dependencies and determine if all courses can be scheduled without cyclic dependencies.

7.0 Algorithm Specification


8.0 Developing A Program
Program in main file methods.

9.0 Analysis of The Algorithm’s Correctness

4.1.1 Kahn's algorithm for topological sorting (Python)
The time complexity analysis provided for the `create_top_sort` method is correct:

- Calculating in-degrees and enqueuing nodes with in-degree 0 both take O(|V| + |E|) time.
- Performing topological sorting takes O(|V| + |E|) time in the worst case.
- Creating a new graph and copying node data both take O(|V|) time.

Therefore, the overall time complexity of the `create_top_sort` method remains O(|V| + |E|).

As for the best, worst, and average cases, here's a breakdown:

- Best Case: In the best case scenario, the course graph is already in a topologically sorted order, meaning there are no prerequisites, and each node has an in-degree of 0. In this case, the calculations for in-degrees, enqueuing nodes, and topological sorting become trivial, resulting in a time complexity of O(|V|) for creating the topological sort.

- Worst Case: The worst case occurs when each node has a maximum number of prerequisites and the graph has a complex dependency structure. In this case, the calculations for in-degrees, enqueuing nodes, and topological sorting become more involved, resulting in a time complexity of O(|V| + |E|).

- Average Case: The average case time complexity depends on the distribution and structure of the course graph. Without additional information about the specific characteristics of the graphs you expect to encounter, it's challenging to provide a precise average case analysis. However, on average, the time complexity is expected to be closer to O(|V| + |E|), assuming a relatively balanced distribution of prerequisites.

It's important to note that the time complexity analysis assumes that the operations within the loops, such as adding nodes and edges to the graph, are constant time operations. The actual runtime may vary based on the complexity of these operations and other factors related to the implementation or the specific graph structures encountered.


4.1.2 Topological sorting using DFS (Java)

The provided code implements a course scheduling algorithm using a depth-first search (DFS) approach to detect cyclic dependencies among courses. Let's analyze the correctness and time complexity of the algorithm.

Correctness:
The algorithm checks for cyclic dependencies by performing a DFS traversal on the course graph. It uses two boolean arrays, `visited` and `recursionStack`, to keep track of visited nodes and the current recursion stack during the traversal.

The algorithm starts by iterating over each course and calling the `hasCycle` method to check if there is a cycle starting from that course. The `hasCycle` method performs a DFS traversal on the graph, marking visited nodes and updating the recursion stack. If it encounters a visited node that is also present in the recursion stack, a cycle is detected, and the method returns `true`. Otherwise, it continues the DFS traversal until all adjacent courses have been explored.

If the `hasCycle` method returns `true` for any course in the main `canFinish` method, it means that a cycle exists in the course graph, and the algorithm returns `false`, indicating that it is not possible to schedule all courses. Otherwise, it returns `true`, indicating that all courses can be scheduled without any cyclic dependencies.

The `printCourseSchedule` method prints the course schedule if it is possible to schedule all courses. It iterates over the schedule, which is populated during the DFS traversal, and prints the course names in reverse order.

Overall, the algorithm correctly identifies cyclic dependencies and determines if it is possible to schedule all courses without conflicts.

Time Complexity:
The time complexity of the algorithm can be analyzed as follows:

1. Constructing prerequisites: The code iterates over the prerequisite array and performs some array operations. This step takes O(|E|), where |E| is the number of prerequisites.

2. DFS traversal: The `hasCycle` method performs a DFS traversal on the course graph. In the worst case, each course is visited once, and for each course, all its prerequisites are explored. This results in a time complexity of O(|V| + |E|), where |V| is the number of courses and |E| is the number of prerequisites.

3. Printing the course schedule: The `printCourseSchedule` method iterates over the schedule, which has a maximum size of |V| (the number of courses). Hence, the time complexity for printing the course schedule is O(|V|).

Therefore, the overall time complexity of the algorithm is O(|V| + |E|).

Note: The space complexity of the algorithm is O(|V|) as it uses boolean arrays to store visited nodes and the recursion stack, and also a schedule list to store the course schedule.

In summary, the algorithm has a time complexity of O(|V| + |E|), where |V| is the number of courses and |E| is the number of prerequisites. It correctly identifies cyclic dependencies and determines if it is possible to schedule all courses without conflicts.

10.0 Online Portfolio




















