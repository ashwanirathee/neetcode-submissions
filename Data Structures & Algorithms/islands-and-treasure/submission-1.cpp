class Solution {
public:
    int n, m;
    std::vector<std::pair<int, int>> coordinates;
    bool pairInVector(const std::vector<std::pair<int, int>>& vec, const std::pair<int, int>& target) {
        for (const auto& pair : vec) {
            if (pair == target) {
                return true;
            }
        }
        return false;
    }
    bool inside(int i, int j) {
        return (0<=i)&&(i<n)&&(0<=j)&&(j<m);
    }
    void dfs(int i, int j, vector<vector<int>>& grid, int dist){
        if (!inside(i, j)) return;
        if(grid[i][j] == -1){
            return;
        } else if (grid[i][j]==0){
            std::cout << "New loc!" << std::endl;
            if(dist == 0){
                dfs(i+1,j, grid, dist + 1);
                dfs(i,j+1, grid, dist + 1);
                dfs(i-1,j, grid, dist + 1);
                dfs(i,j-1, grid, dist + 1);
            }
            else{
                std::pair<int, int> target = {i, j};
                if(pairInVector(coordinates, target)!=0)
                {
                    std::cout << "Going back, not visited" << i << " " << j << std::endl;
                    return;
                } 
            }
        } else if (grid[i][j]==2147483647 || grid[i][j] > dist){
            std::cout << "New dfs round" << std::endl;
            grid[i][j]=min(dist, grid[i][j]);
            dfs(i+1,j, grid, dist + 1);
            dfs(i,j+1, grid, dist + 1);
            dfs(i-1,j, grid, dist + 1);
            dfs(i,j-1, grid, dist + 1);
        }
    }
    void islandsAndTreasure(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 0){
                    coordinates.push_back(std::make_pair(i, j));
                    std::cout << "Starting new Loc:" << i << " " << j << std::endl;
                    dfs(i,j, grid, 0);
                }
            }
        }
    }
};
