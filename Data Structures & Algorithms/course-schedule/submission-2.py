class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            adj_list[course].append(prerequisite)

        # 0 = unvisited
        # 1 = currently visiting
        # 2 = fully processed
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for prerequisite in adj_list[course]:
                if not dfs(prerequisite):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
