import java.util.ArrayList;
import java.util.List;

class CourseScheduler2 {
    private int numCourses;
    private List<int[]> prerequisites;
    private List<int[]> schedule;
    private boolean[] visited;
    private boolean[] recursionStack;

    public CourseScheduler2(int numCourses, int[][] prerequisites) {
        this.numCourses = numCourses;
        this.prerequisites = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            this.prerequisites.add(new int[0]);
        }
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prerequisiteCourse = prerequisite[1];
            int[] coursePrerequisites = this.prerequisites.get(course);
            int[] updatedPrerequisites = new int[coursePrerequisites.length + 1];
            System.arraycopy(coursePrerequisites, 0, updatedPrerequisites, 0, coursePrerequisites.length);
            updatedPrerequisites[coursePrerequisites.length] = prerequisiteCourse;
            this.prerequisites.set(course, updatedPrerequisites);
        }
        schedule = new ArrayList<>();
        visited = new boolean[numCourses];
        recursionStack = new boolean[numCourses];
    }

    public boolean canFinish() {
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i] && hasCycle(i)) {
                return false;
            }
        }
        return true;
    }

    private boolean hasCycle(int course) {
        visited[course] = true;
        recursionStack[course] = true;

        for (int nextCourse : prerequisites.get(course)) {
            if (!visited[nextCourse]) {
                if (hasCycle(nextCourse)) {
                    return true;
                }
            } else if (recursionStack[nextCourse]) {
                return true;
            }
        }

        recursionStack[course] = false;
        schedule.add(0, new int[] { course });
        return false;
    }

    public void printCourseSchedule() {
        if (canFinish()) {
            System.out.println("Course Schedule:");
            int numCourses = schedule.size();
            for (int i = numCourses - 1; i >= 0; i--) {
                int courseId = schedule.get(i)[0];
                System.out.print(getCourseName(courseId));
                if (i > 0) {
                    System.out.print(" -> ");
                }
            }
            System.out.println();
        } else {
            System.out.println("Unable to schedule all courses due to cyclic dependencies.");
        }
    }

    private String getCourseName(int courseId) {
        // Map course IDs to course names
        // Modify this method according to your course naming convention
        String[] courses = { "Maths", "English", "Physics", "Chemistry", "Computer Science", "Biology" };
        //                      0         1           2           3               4              5
        return courses[courseId];
    }
}

public class CourseSchedulerMain {
    public static void main(String[] args) {
        int numCourses = 6;
        int[][] prerequisites = { { 4, 1 }, {4 , 5}, { 4, 0 }, { 5, 2 }, { 5, 0 }, { 2, 3 }, { 3, 1 } };

        CourseScheduler2 scheduler = new CourseScheduler2(numCourses, prerequisites);
        scheduler.printCourseSchedule();
    }
}