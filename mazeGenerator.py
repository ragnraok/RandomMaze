#A maze generator
from random import randint

def make_maze(width, height, density=0.9, complexity=1.8):
        """
        Note: width is columns number, height is row number
        """
        shape_width = (width//2)*2+1
        shape_height = (height//2)*2+1
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

        print 'the path track is'
        return (maze, path_track)

if __name__ == '__main__':
        maze, path_track = make_maze(5, 5)

        print maze
        print ''
        print path_track

        print path_track[0][0]

                        
            
                       




