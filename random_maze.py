from random import randint

class DisjointSet(object):
        def __init__(self, size):
                self.size = size
                self.set_list = [-1] * size

        def find_root(self, node):
                if self.set_list[node] < 0:
                        return node
                else:
                        return self.find_root(self.set_list[node])
        def uniont_set(self, node1, node2):
                root1 = self.find_root(node1)
                root2 = self.find_root(node2)

                if root1 == root2:
                        return
                if self.set_list[root2] < self.set_list[root1]:
                        self.set_list[root1] = root2
                else:
                        if self.set_list[root1] == self.set_list[root2]:
                                self.set_list[root1] -= 1
                        self.set_list[root2] = root1

        def if_connected(self, node1, node2):
                return self.find_root(node1) == self.find_root(node2)

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
                # it will the separated cell as the nodes
                cell_row_num = (self.height - 3) // 2
                cell_col_num = (self.width - 3) // 2
                
                #print cell_row_num
                #print cell_col_num
        
                path_track = []
        
                maze = [1]*self.height
                for i in range(self.height):
                        maze[i] = [1]*self.width
                
                # let he first row and the last row become False 
                maze[0] = [0]*self.width
                maze[self.height - 1] = [0]*self.width
        
                # let the first column and the last column become False
                for row in maze:
                        row[0] = 0 
                        row[self.width - 1] = 0 
        
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
                maze[2][1] = 0 
                maze[2*cell_row_num][2*cell_col_num + 1] = 0
        
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
        
                maze[next_row][next_col] = 0
                path_track.append((next_row, next_col))
        
                next_index = randint(0, 3)
                
                for i in range(4):
                        if maze[next_row + 2 * direction[next_index][0]][next_col + 2 * direction[next_index][1]] == 1:
                                maze[next_row + direction[next_index][0]][next_col + direction[next_index][1]] = 0
                                path_track.append((next_row + direction[next_index][0], next_col + direction[next_index][1]))
                                self.__dfs(row + direction[next_index][0], col + direction[next_index][1], maze, path_track)
        
                        next_index = (next_index + 1) % 4

        def pos_to_list(self, row, col):
                """
                row and col is one based
                """
                cell_col_num = (self.width - 3) // 2
                return (row - 1) * cell_col_num + (col - 1)
        
        def disjoint_make_maze(self):
                direction = [
                        (0, 1),
                        (0, -1),
                        (1, 0),
                        (-1, 0)]
        
                #True is wall, False is road
                maze = [1] * self.height
                for i in range(self.height):
                        maze[i] = [1]*self.width

                path_track = []
        
                #set the borders
                maze[0] = [0] * self.width
                maze[self.height - 1] = [0] * self.width
        
                for i in range(self.height):
                        maze[i][0] = 0 
                        maze[i][self.width - 1] = 0 

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
        
                cell_row_num = (self.height - 3) // 2 #view the cell as wall
                cell_col_num = (self.width - 3) // 2
        
                #print 'cell_row_num = ' + str(cell_row_num) + ' cell_col_num = ' + str(cell_col_num)
        
                start_pos = (1, 1)
                end_pos = (cell_row_num, cell_col_num)
                maze[2][1] = 0 
                maze[cell_row_num * 2][cell_col_num * 2 + 1] = 0

                path_track.append((2, 1))
                path_track.append((cell_row_num * 2, cell_col_num * 2 + 1))
        
                disjoint_set = DisjointSet(cell_row_num * cell_col_num)
        
                start_index = self.pos_to_list(start_pos[0], start_pos[1])
                end_index = self.pos_to_list(end_pos[0], end_pos[1])
        
                while not disjoint_set.if_connected(start_index, end_index):
                        rand_direction = direction[randint(0, len(direction) - 1)]
        
                        rand_row = randint(1, cell_row_num)
                        rand_col = randint(1, cell_col_num)
        
                        #print 'rand_row = ' + str(rand_row) + ' rand_col = ' + str(rand_col)
                        #print 'rand_direction = ' + str(rand_direction)
        
                        if (not 0 < rand_row + rand_direction[0] <= cell_row_num) or \
                           (not 0 < rand_col + rand_direction[1] <= cell_col_num):
                                #print 'continue'
                                continue
                        
                        if maze[rand_row * 2 + rand_direction[0]][rand_col * 2 + rand_direction[1]] == 1:
                                # let it become the cell...
                                maze[rand_row * 2][rand_col * 2] = 0
                                maze[rand_row * 2 + rand_direction[0] * 2][rand_col * 2 + rand_direction[1] * 2] = 0

                                path_track.append((rand_row * 2, rand_col * 2))
                                path_track.append((rand_row * 2 + rand_direction[0] * 2, rand_col * 2 + rand_direction[1] * 2))

                                node1 = self.pos_to_list(rand_row, rand_col)
                                node2 = self.pos_to_list(rand_row + rand_direction[0], rand_col + rand_direction[1])
        
                                #print 'node1 = ' + str(node1) + ', node2 = ' + str(node2)
        
                                if not disjoint_set.if_connected(node1, node2):
                                        # pull down the wall
                                        maze[rand_row * 2 + rand_direction[0]][rand_col * 2 + rand_direction[1]] = 0
                                        disjoint_set.uniont_set(node1, node2)

                                        path_track.append((rand_row * 2 + rand_direction[0], rand_col * 2 + rand_direction[1]))
        
                
                return maze, path_track
