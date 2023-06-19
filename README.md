# CSC4202-G1-Project


## 1. Introduction: (1 min) (ramesh)
#very Brief overview of the university course scheduling problem scenario.
#brief model development


## 2. Problem Description:  (1 min) (syakila)
#Explain the different sub-problems of university course scheduling, emphasizing which we choose

a. Time conflicts
b.  [Topological] Prerequisite dependencies
c.  [Knapsack] Course availability (capacity)
d. [Topological] Credit constraints 
e. Student preferences

#mention how we focus on these three 
#mention how we tried doing c cuz to implement this we just use knapsack which is in syllabus but we not satisfied cuz a schedule prioritize prerequisites and credit constraints more
#next we decide to do b because it suits our scenario the most (with add ons of c)


## 3. Algorithm Selection: (2 min) (qistina)
#Discuss the various solution paradigms, such as sorting, divide and conquer, dynamic programming, greedy algorithms, and graph algorithms. 
#justify why you chose the graph algorithm (topological sorting) as the suitable solution.

## 4. Topological Sorting (3 min) (ramesh)
#Provide a detailed explanation of how topological sorting works,
#emphasizing its ability to handle prerequisite dependencies efficiently. 
#Discuss its relevance to the course scheduling problem and how it addresses the goals and constraints.

## 5. Implementation Overview: (3 min) (mugi/ syakila)
#said la how we tried implementing using dfs of topological algorithm juga
#then said we decide to choose the khan’s/ dag approach bc its more suitable for prerequisites problem
#show code and especially focuses on part that have topological sorting
#Briefly describe the implementation approach for the topological sorting algorithm.
#Highlight the data structures and any additional techniques used to handle credit constraints and other requirements.

## 6. Code Demonstration: (1 min?) (mugi/ syakila)
#Present the code demonstration (video or real time??)
#also show how the java one works 
#Use visual aids, such as code snippets, diagrams, or slides, to enhance understanding. Keep the demonstration concise and focused on the key aspects of the algorithm.

## 7. Time complexity: (3) (qistina/ mugi)
#Time complexity of specific part of algorithm (important) python
#kalau sempat baru explain the java one
#Time complexity of whole system (just briefly)

## 8. Conclusion and Q&A: (1 min) (syakila)
#Summarize the main points covered in the presentation, emphasizing the significance of the problem and the suitability of the solution. Conclude by opening the floor for questions from the audience.

