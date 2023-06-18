#  Title:		Graph and schedule implementation
#  Purpose:     This class creates a graph from the processed csv input. It is then sorted using a topological sort,
#                   eventually being used to create the class schedule.
# 
#  TC:          O(n^3)
import networkx as nx
import matplotlib.pyplot as plt
import re

class Graph:
    def __init__(self):
        self.course_graph = None
        self.top_graph = None

    def create_graph(self, course_input):
        # Create a directed graph and add nodes and edges based on course prerequisites
        graph = nx.DiGraph()
        for course, course_data in course_input.items():
            graph.add_node(course)
            for prerequisite in course_data[2]:
                if len(prerequisite) == 0:
                    continue
                optionals = prerequisite.split(' | ')
                if len(optionals) != 0:
                    for optional in optionals:
                        graph.add_edge(optional, course)
                else:
                    graph.add_edge(prerequisite, course)

        # Add data to each node in the graph
        for course in graph.nodes:
            course_name, credits, prerequisites, semesters_offered = course_input[course]
            graph.nodes[course]["data"] = (course_name, credits, prerequisites, semesters_offered)

        self.course_graph = graph

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

    def draw_graph(self):
        # Draw the topological graph using the Spring layout algorithm
        pos = nx.spring_layout(self.top_graph, k=5)
        nx.draw(self.top_graph, pos=pos, with_labels=True, arrows=True)
        plt.show()

    def create_schedule(self, desired_credits, start_sem):
        schedule = {}
        year = {"Semester 1": [], "Semester 2": []}
        creds_per_q = [0, 0, 0]
        curr_year = 1
        i = 0

        # Validate and set the desired credits and starting semester
        desired_credits = int(desired_credits) if desired_credits.isdigit() and int(desired_credits) in range(12, 19) else 18
        start_sem = int(start_sem) if start_sem.isdigit() and int(start_sem) in range(1, 8) else 1

        nodes = self.top_graph.nodes()
        list_nodes = list(nodes)

        while len(list_nodes) != 0:
            course = list_nodes[i]
            course_name, credits, prerequisites, semesters_offered = nodes[course]['data']
            credits = int(credits)

            course_year = int(re.sub('\D', '', course)[0]) - 1

            good_to_go = True
            for prerequisite in prerequisites:
                optionals = prerequisite.split(' | ')
                if len(optionals) > 1:
                    for option in optionals:
                        if option in list_nodes:
                            good_to_go = False
                        else:
                            good_to_go = True
                            break
                else:
                    if prerequisite in list_nodes:
                        good_to_go = False

            if (not good_to_go) and prerequisites[0] != '' or curr_year < course_year:
                i += 1
            else:
                for quarter in year:
                    curr_sem = int(quarter[-1])
                    if curr_year == 1 and curr_sem < start_sem:
                        continue
                    if str(curr_sem) not in semesters_offered:
                        continue
                    if creds_per_q[curr_sem - 1] + credits > desired_credits:
                        continue
                    year[quarter].append(course)
                    creds_per_q[curr_sem - 1] += credits
                    list_nodes.pop(i)
                    break
                else:
                    i += 1

            if i >= len(list_nodes) or sum(creds_per_q) == desired_credits * 3:
                i = 0
                schedule["Year " + str(curr_year)] = year
                curr_year += 1
                creds_per_q = [0, 0, 0]
                year = {"Semester 1": [], "Semester 2": []}

        return schedule
