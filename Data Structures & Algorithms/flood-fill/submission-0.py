class Solution:
    def floodFillHelper(self, image, sr, sc, color, og_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return 

        print(sr, sc)
        if image[sr][sc] != og_color:
            return
        
        image[sr][sc] = color
        self.floodFillHelper(image, sr-1, sc, color, og_color)
        self.floodFillHelper(image, sr+1, sc, color, og_color)
        self.floodFillHelper(image, sr, sc-1, color, og_color)
        self.floodFillHelper(image, sr, sc+1, color, og_color)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.floodFillHelper(image, sr, sc, color, image[sr][sc])
        return image