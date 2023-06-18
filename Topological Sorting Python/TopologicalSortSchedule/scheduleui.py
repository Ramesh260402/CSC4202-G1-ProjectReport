#  Title:		Visualize graph implementation
#  Purpose:     Creates a visual of the course schedule that is generated in graph.py. 
#                   It adapts for the starting quarter and credit limit, and shows all the courses, along with
#                   their pre-reqs in a quarter separated fashion.
# 
#  TC:          O(n^3)
import matplotlib.pyplot as plt
from reader import Reader

class GraphUI:
    def __init__(self, course_data, file_reader) -> None:
        self.courses_dict = course_data
        self.read_major = file_reader
    
    def create_graph(self):
        # define courses and quarters
        courses = self.read_major.courseDict.keys()
        quarters = {}
        pos = {}
        qtr_count = 0
        prev_classes = set()
        total_semesters = []
        
        for y in self.courses_dict:
            for q in self.courses_dict[y]:
                qtr_count += 1
                qtr = 'Sem ' + str(qtr_count)
                total_semesters.append(qtr)
                quarters[qtr] = self.courses_dict[y][q]
                y_pos_count = 1
                
                for c in self.courses_dict[y][q]:
                    pos[c] = (qtr_count * 2.25, y_pos_count * 3)
                    y_pos_count += 1
                
                prev_classes.update(self.courses_dict[y][q])

        if len(total_semesters) < ((len(prev_classes) // 2) - 1):
            while len(total_semesters) < ((len(prev_classes) // 2) - 1):
                total_semesters.append('')
        else:
            prev_classes = list(prev_classes)
            while len(total_semesters) != ((len(prev_classes) // 2) - 1):
                prev_classes.append('')

        fig, ax = plt.subplots(figsize=(10, 8), facecolor='#CCE5FF')
        fig.subplots_adjust(left=.1, bottom=.1, right=.9, top=.9)

        ax.set_facecolor('#DFDBE6')

        for course in courses:
            quarter = None
            for q, c_list in quarters.items():
                if course in c_list:
                    ax.add_patch(plt.Circle(pos[course], radius=.7, facecolor='lightblue', edgecolor='darkblue'))
                    ax.text(pos[course][0], pos[course][1], course, ha='center', va='center', size=10, color='black')

        ax.set_xlim(0, len(prev_classes) * 1.1)
        ax.set_ylim(0, 16)
        ax.set_aspect('equal')
        total_semesters.insert(0, '')

        plt.xticks([i * 2.25 for i in range(len(prev_classes) // 2)], total_semesters)
        plt.gca().get_yaxis().set_visible(False)
        fig.canvas.manager.full_screen_toggle()
        ax.axis('scaled')

        # Add the title above the plot with custom font size and font family
        plt.title('Course Schedule', fontdict={'fontsize': 16, 'fontfamily': 'Monospace'})
 
        plt.show()
