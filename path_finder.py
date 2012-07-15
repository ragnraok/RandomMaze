from random_maze import RandomMaze

class MazePathFinder(object):
        def __init__(self, maze, start_pos, end_pos, row_num, col_num):
                """
                the maze:
                        1 denote wall, 0 denote road
                        and the borders are all 0
                the maze must be solvable
                start_pos: the start position tuple(row, col)
                end_pos: the end position tuple(row, col)
                """
                self.maze = maze
                self.start_pos = start_pos
                self.end_pos = end_pos
                self.row_num = row_num
                self.col_num = col_num
                    
        def __if_pos_valid(self, row, col):
                # check the index range
                if row < 0 or row >= self.row_num or col < 0 or col >= self.col_num:
                        return False
                #  check if borders
                elif row == 0 or row == self.row_num - 1:
                        return False
                elif col == 0 or col == self.col_num - 1:
                        return False
                # then check if wall
                elif self.maze[row][col] == 1:
                        return False
                # then check if visited, which is marked as -1
                elif self.maze[row][col] == -1:
                        return False
                return True

        def bfs_find_path(self):
                """
                use BFS to find the shortest path from start_pos to end_pos
                """
                direction = [
                        (0, 1),
                        (0, -1),
                        (1, 0),
                        (-1, 0)]
                path_queue = [tuple(self.start_pos)]
                self.maze[self.start_pos[0]][self.start_pos[1]] = -1

                if_find = False

                record = [(0, 0)]*self.row_num
                for i in range(self.row_num):
                        record[i] = [(0, 0)]*self.col_num

                while len(path_queue) > 0 and not if_find:
                        cur_pos = path_queue[0]
                        del path_queue[0]
                        #print cur_pos
                        self.maze[cur_pos[0]][cur_pos[1]] = -1

                        for i in range(4):
                                next_dir = direction[i]
                                next_pos = (cur_pos[0] + next_dir[0], cur_pos[1] + next_dir[1])
                                #print next_pos
                                if self.__if_pos_valid(next_pos[0], next_pos[1]):
                                        self.maze[next_pos[0]][next_pos[1]] = -1
                                        path_queue.append(next_pos)

                                        # mark the precursor
                                        record[next_pos[0]][next_pos[1]] = cur_pos

                                        if next_pos[0] == self.end_pos[0] and next_pos[1] == self.end_pos[1]:
                                                if_find = True
                                                break
                if if_find:
                        path = []
                        start_row = self.start_pos[0]
                        start_col = self.start_pos[1]
                        end_row = self.end_pos[0]
                        end_col = self.end_pos[1]

                        cur_row = end_row
                        cur_col = end_col

                        path.append(self.end_pos)

                        #print record
                        
                        while cur_row != start_row or cur_col != start_col:
                                row = cur_row
                                col = cur_col
                                cur_row = record[row][col][0]
                                cur_col = record[row][col][1]
                                path.append((cur_row, cur_col))

                        print path_queue
                        print path

                        return path
                else:
                        print 'no path find'
                        return []

if __name__ == '__main__':
        row = 11
        col = 11
        cell_row_num = (row - 3) // 2
        cell_col_num = (col - 3) // 2
        rand_maze = RandomMaze(row, col)
        maze, path_track = rand_maze.dfs_maze()

        path_finder = MazePathFinder(maze, (2, 1), (2 * cell_row_num, 2 * cell_col_num + 1), row, col)

        path_queue = path_finder.bfs_find_path()
        
        for i in range(len(maze)):
                print maze[i]

        print path_queue

        


