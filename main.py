from gridview import GridView
from random_maze import RandomMaze
from path_finder import MazePathFinder

import pygame
from pygame.locals import *
from sys import exit
import sys

pygame.init()

width = 984
height = 504
grid_size = 24

background_color = (230, 230, 100)
grid_line_color = (0, 0, 0)
cell_color = (50, 50, 255)
path_color = (255, 50, 50)

resolution = (width, height)

ran_maze = RandomMaze(width//grid_size, height//grid_size)

cell_row_num = (height//grid_size - 3) // 2
cell_col_num = (width//grid_size - 3) // 2

def get_maze_method(option):
        if option == 1:
            return ran_maze.dfs_maze
        elif option == 2:
            return ran_maze.disjoint_make_maze
        else:
                return None

def main(maze_method, speed=0.010, mode=0):
        """
        the main program of the program
        mode 0: default mode, build the wall
        mode 1: first all cell are wall, then pull down the wall
        """
        screen = pygame.display.set_mode(resolution, 0, 32)
        clock = pygame.time.Clock()
        maze, cell_list = maze_method()

        path_finder = MazePathFinder(maze, (2, 1), (cell_row_num * 2, cell_col_num * 2 + 1), 
                              height//grid_size, width//grid_size)
        path = path_finder.bfs_find_path()

        index = 0
        path_index = 0
        maze_finished = False

        pass_time = 0
        grid_view = GridView(screen, width, height, grid_size, grid_line_color) 
        while True:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                exit()

                press_key = pygame.key.get_pressed()
                
                # press F5 to regenerate the maze
                if press_key[K_F5]:
                        index = 0
                        path_index = 0
                        maze, cell_list = maze_method()
                        path_finder = MazePathFinder(maze, (2, 1), (cell_row_num * 2, cell_col_num * 2 + 1), 
                                height//grid_size, width//grid_size)
                        path = path_finder.bfs_find_path()
                        maze_finished = False

                #print index
                
                if mode == 0:
                    screen.fill(background_color)
                else:
                        screen.fill(cell_color)

                # draw the cell
                for i in range(index + 1):
                        if mode == 0:
                            grid_view.fill_a_cell(cell_list[i][1], cell_list[i][0], cell_color)
                        else:
                            grid_view.fill_a_cell(cell_list[i][1], cell_list[i][0], background_color)

                # draw the grid
                grid_view.draw()

                # draw the path
                if maze_finished and path:
                        for i in range(path_index + 1):
                                grid_view.fill_a_cell_with_circle(path[len(path) - i - 1][1], 
                                                                  path[len(path) - i - 1][0], path_color)

                time_passed_seconds = clock.tick() / 1000.0
                pass_time += time_passed_seconds

                if pass_time >= speed:
                        pass_time = 0
                        if maze_finished:
                                if path_index + 1 < len(path):
                                        path_index += 1

                        if index >= len(cell_list) - 1:
                                #print 'maze_finished'
                                maze_finished = True
                                
                        if index + 1 < len(cell_list):
                                index += 1

                pygame.display.update()

def parser_arg(argv):
        """
        parser the arguments,
        python main.py [OPTION]:
                -d --dfs: use dfs algorithm to generate the maze, and return 1(default value)
                -k --kruscal: use kruscal algorithm to generate the maze, and return 2
        """
        args = argv[1:]
        if len(args) == 0:
                return 1
        elif len(args) > 1:
                print 'Error option'
                print 'Usage:'
                print "(python) main.py [OPTION]: \n" + \
                "  -d --dfs: use dfs algorithm to generate the maze(default option)\n" +\
                "  -k --kruscal: use kruscal algorithm to generate the maze "
                return 0
        elif args[0] == '-d' or args[0] == '--dfs':
                return 1
        elif args[0] == '-k' or args[0] == '--kruscal':
                return 2
        else:
                print 'Error option'
                print 'Usage:'
                print "(python) main.py [OPTION]: \n" + \
                "  -d --dfs: use dfs algorithm to generate the maze(default option)\n" +\
                "  -k --kruscal: use kruscal algorithm to generate the maze "
                return 0


if __name__ == '__main__':
        method = get_maze_method(parser_arg(sys.argv))
        if method:
            main(maze_method = get_maze_method(parser_arg(sys.argv)), mode = 1)
                                        
