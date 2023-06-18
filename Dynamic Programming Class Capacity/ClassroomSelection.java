import java.util.Arrays;

public class ClassroomSelection {
    public static void main(String[] args) {
        int[] classCapacity = {10, 20, 30, 40, 50}; // Capacity of each class
        int totalStudents = 50; // Total number of students

        String[] classNames = {"A", "B", "C", "D", "E"}; // Class names

        int[][] dp = new int[classCapacity.length + 1][totalStudents + 1];

        // Initialize the table with a large value
        int largeValue = totalStudents + 1;
        for (int i = 0; i <= classCapacity.length; i++) {
            Arrays.fill(dp[i], largeValue);
        }

        // Base case: If there are no students, no classrooms are needed
        for (int i = 0; i <= classCapacity.length; i++) {
            dp[i][0] = 0;
        }

        // Fill the table using dynamic programming
        for (int i = 1; i <= classCapacity.length; i++) {
            for (int j = 1; j <= totalStudents; j++) {
                // If the current class can accommodate j students
                if (classCapacity[i - 1] <= j) {
                    dp[i][j] = Math.min(dp[i - 1][j], 1 + dp[i][j - classCapacity[i - 1]]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

     // Find the class with the minimum excess capacity (closest to the total number of students)
        int bestClassIndex = -1;
        int minExcessCapacity = Integer.MAX_VALUE;
        for (int i = 0; i < classCapacity.length; i++) {
            int excessCapacity = classCapacity[i] - totalStudents;
            if (excessCapacity >= 0 && excessCapacity < minExcessCapacity) {
                minExcessCapacity = excessCapacity;
                bestClassIndex = i;
            }
        }

        // Print the best class if found
        if (bestClassIndex != -1) {
            String bestClass = classNames[bestClassIndex];
            System.out.println("Best Class: " + bestClass);
            System.out.println("Minimum Classrooms Required: 1");
        } else {
            System.out.println("No valid class found.");
        }

    }
}