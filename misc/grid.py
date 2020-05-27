import copy

def get_path(maze, r, c, path):
    if r < 0 or c < 0 or not maze[r][c]:
        return False
    isOrigin = (r == 0  and c == 0)
    if isOrigin or get_path(maze, r - 1, c, path) or get_path(maze, r, c - 1, path):
        path.append((r, c))
        return True
    return False

def get_all_path(maze, r, c, cur_path, paths):
    if r < 0 or c < 0 or not maze[r][c]:
        return
    isOrigin = (r == 0  and c == 0)
    if isOrigin:
        cur_path.append((r, c))
        paths.append(cur_path)
        return
    new_path = copy.deepcopy(cur_path)
    new_path.append((r, c))
    get_path(maze, r - 1, c, new_path, paths)
    new_path = copy.deepcopy(cur_path)
    new_path.append((r, c))
    get_path(maze, r, c - 1, new_path, paths)
    
def get_all_path2(maze, r, c, cur_path, paths):
    if r < 0 or c < 0 or not maze[r][c]:
        return
    isOrigin = (r == 0  and c == 0)
    if isOrigin:
        cur_path.append((r, c))
        paths.append(cur_path)
        return
    path.append((r, c))
    get_path(maze, r - 1, c, path, paths)
    path.pop()
    path.append((r, c))
    get_path(maze, r, c - 1, path, paths)
    path.pop()
    
    

if __name__ == '__main__':
maze = [[True, True, True, True], [True, False, True, True], [True, True, True, True]]
visited = [[False, False, False], [False, False, False], [False, False, False]]
paths = []
get_path(maze, 2, 3, [], paths)
print(paths)
    
