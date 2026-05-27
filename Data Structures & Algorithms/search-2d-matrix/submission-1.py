class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        curr_mid = nums[mid]

        if curr_mid < target:
            result = self.search(nums[mid+1:], target)
            if result == -1:
                return -1
            return mid + 1 + result
        elif curr_mid > target:
            return self.search(nums[:mid], target)
        else:
            return mid

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if len(matrix) == 0:
            return False
        n = len(matrix[0])
        # print(m,n)

        m_i=0
        m_j=m

        n_i = 0
        n_j = n

        m_mid = m // 2
        res = False
        if matrix[m_mid][0] > target:
            m_j = m_mid
            # print(m_i, m_j)
            # print(matrix[m_i:m_j])
            res = self.searchMatrix(matrix[m_i:m_j], target)
        elif matrix[m_mid][-1] < target:
            m_i = m_mid+1
            # print(m_i, m_j)
            # print(matrix[m_i:m_j])
            res = self.searchMatrix(matrix[m_i:m_j], target)
        else: 
            # binary_search
            # print("in this")
            res = self.search(matrix[m_mid], target)
            if res != -1:
                return True
            else:
                return False

        return res