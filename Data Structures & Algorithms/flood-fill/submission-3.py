class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = [[-1,0],[1,0],[0,1],[0,-1]]
        og = image[sr][sc]
        if image[sr][sc]== color:
            return image
        image[sr][sc]= color
        rows = len(image)
        cols =len(image[0])
        
        # print(sr,sc)
        for p, q in n:
            ni = sr + p
            nj = sc + q
            if 0<=ni<rows and 0<=nj<cols and og == image[ni][nj]:
                self.floodFill(image,ni, nj, color=color)

        return image