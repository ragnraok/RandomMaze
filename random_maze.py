from random import randint

class RandomMaze(object):
        def __init__(self, width, height):
                """
                A random Maze generator
                width is the columns number, height is row number
                """
                self.width = width
                self.height = height

        def simply_maze(self, density=0.9, complexity=1.8):
            """
            A simple algorithm used to generate a maze
            """
            shape_width = (self.width//2)*2+1
            shape_height = (self.height//2)*2+1
            complexity = int(complexity*(5*(shape_height+shape_width)))
            density    = int(density*(shape_height//2*shape_height//2))

            path_track = []
            # let maze become a height * width matrix
            maze = [False]*shape_height
            for i in range(shape_height):
                    maze[i] = [False]*shape_width

            # fill the borders 
            maze[0] = [True]*shape_width # first row
            maze[shape_height - 1] = [True]*shape_width # the last row
            # the first column and the last column
            for row in maze:
                    row[0] = True
                    row[shape_width - 1] = True

            # in the path_track list, add the borders cells
            # first row
            for i in range(shape_width):
                    path_track.append((0, i))

            # the last column
            for i in range(1, shape_height - 1):
                    path_track.append((i, shape_width - 1))

            # the last row
            for i in reversed(range(shape_width)):
                    path_track.append((shape_height - 1, i))

            # the first column
            for i in reversed(range(1, shape_height - 1)):
                    path_track.append((i, 0))

            path_track.append((0,0))

            #the start_point is [1,1]
            #start_point = (1, 1)
            #x = start_point[0] # x coordinate, that is, columun No.
            #y = start_point[1] # y coordinate, that is, row No.

            # make the maze
            for i in range(density):
                    x = randint(0, shape_width//2)*2
                    y = randint(0, shape_height//2)*2
                    maze[y][x] = True
                    path_track.append((y, x)) # the index of draw grid               
                    for j in range(complexity):
                            neighbour = []
                            if x > 1:
                                    neighbour.append((y, x - 2))
                            if x < shape_width - 2:
                                    neighbour.append((y, x + 2))
                            if y > 1:
                                    neighbour.append((y - 2, x))
                            if y < shape_height - 2:
                                    neighbour.append((y + 2, x))
                            if len(neighbour) > 0:
                                    next_y, next_x = neighbour[randint(0, len(neighbour) - 1)]
                                    if maze[next_y][next_x] == False:
                                            maze[next_y][next_x] = True
                                            path_track.append((next_y, next_x))
                                            maze[next_y+(y-next_y)//2][next_x+(x-next_x)//2] = True
                                            path_track.append((next_y+(y-next_y)//2, next_x+(x-next_x)//2))
                                            x = next_x
                                            y = next_y
            
                    #x = randint(0, shape_width//2)*2
                    #y = randint(0, shape_height//2)*2

            #print 'the path track is'
            #print path_track
            return (maze, path_track)
    
        def dfs_maze(self):
                """
                width is the grid columns number
                height is the grid rows number
                """
                # it will the separated cell as the nodes
                cell_row_num = (self.height - 3) // 2
                cell_col_num = (self.width - 3) // 2
                
                #print cell_row_num
                #print cell_col_num
        
                path_track = []
        
                maze = [True]*self.height
                for i in range(self.height):
                        maze[i] = [True]*self.width
                
                # let he first row and the last row become True
                maze[0] = [False]*self.width
                maze[self.height - 1] = [False]*self.width
        
                # let the first column and the last column become True
                for row in maze:
                        row[0] = False 
                        row[self.width - 1] = False
        
                # also, set up the path_track list
                # the first row
                for i in range(self.width):
                        path_track.append((0,i))
                
                # the last column
                for i in range(1, self.height - 1):
                        path_track.append((i, self.width - 1))
        
                # the last row
                for i in reversed(range(self.width)):
                        path_track.append((self.height - 1, i))
        
                # the first column
                for i in reversed(range(1, self.height - 1)):
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
        
                self.__dfs(rand_start_row, rand_start_col, maze, path_track)
        
                return maze, path_track

        def __dfs(self, row, col, maze, path_track):
                direction = [
                        (0,1),
                        (1,0),
                        (0,-1),
                        (-1,0)
                ]

                next_row = row * 2
                next_col = col * 2
                #print 'next_row = ' + str(next_row) + ' next_col = ' + str(next_col)
        
                maze[next_row][next_col] = False
                path_track.append((next_row, next_col))
        
                next_index = randint(0, 3)
                
                for i in range(4):
                        if maze[next_row + 2 * direction[next_index][0]][next_col + 2 * direction[next_index][1]] == True:
                                maze[next_row + direction[next_index][0]][next_col + direction[next_index][1]] = False
                                path_track.append((next_row + direction[next_index][0], next_col + direction[next_index][1]))
                                self.__dfs(row + direction[next_index][0], col + direction[next_index][1], maze, path_track)
        
                        next_index = (next_index + 1) % 4

