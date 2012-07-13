#the dfs algorithm test
from random import randint

def dfs_make_maze(width, height):
        """
        width is the grid columns number
        height is the grid rows number
        """
        # it will the separated cell as the nodes
        cell_row_num = (height - 3) // 2
        cell_col_num = (width - 3) // 2
        
        #print cell_row_num
        #print cell_col_num

        path_track = []

        maze = [True]*height
        for i in range(height):
                maze[i] = [True]*width
        
        # let he first row and the last row become True
        maze[0] = [False]*width
        maze[height - 1] = [False]*width

        # let the first column and the last column become True
        for row in maze:
                row[0] = False 
                row[width - 1] = False

        # also, set up the path_track list
        # the first row
        for i in range(width):
                path_track.append((0,i))
        
        # the last column
        for i in range(1, height - 1):
                path_track.append((i, width - 1))

        # the last row
        for i in reversed(range(width)):
                path_track.append((height - 1, i))

        # the first column
        for i in reversed(range(1, height - 1)):
                path_track.append((i, 0))

        # determinated the entry and the exit
        maze[2][1] = False
        maze[2*cell_row_num][2*cell_col_num + 1] = False

        path_track.append((2, 1))
        path_track.append((2*cell_row_num, 2*cell_col_num + 1))

        # also, set up the path_track list

        rand_start_row = randint(1, cell_row_num)
        rand_start_col = randint(1, cell_col_num)

        #print 'start_row = ' + str(rand_start_row) + ' start_col = ' + str(rand_start_col)

        dfs(rand_start_row, rand_start_col, maze, path_track)

        return maze, path_track

direction = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
]

def dfs(row, col, maze, path_track):
        next_row = row * 2
        next_col = col * 2
        #print 'next_row = ' + str(next_row) + ' next_col = ' + str(next_col)

        maze[next_row][next_col] = False
        path_track.append((next_row, next_col))

        turn = randint(0,1) and 1 or 3
        next_index = randint(0, 3)
        
        for i in range(4):
                if maze[next_row + 2 * direction[next_index][0]][next_col + 2 * direction[next_index][1]] == True:
                        maze[next_row + direction[next_index][0]][next_col + direction[next_index][1]] = False
                        path_track.append((next_row + direction[next_index][0], next_col + direction[next_index][1]))
                        dfs(row + direction[next_index][0], col + direction[next_index][1], maze)

                next_index = (next_index + turn) % 4
        
if __name__ == '__main__':
        maze, path_track = dfs_make_maze(5, 5)
        print maze
        print path_track
