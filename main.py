from gridview import GridView
from random_maze import RandomMaze

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 984
height = 504
grid_size = 24

background_color = (230, 230, 100)
grid_line_color = (0, 0, 0)
cell_color = (50, 50, 255)

resolution = (width, height)

ran_maze = RandomMaze(width//grid_size, height//grid_size)

def get_maze_method(argv):
        #return ran_maze.simply_maze
        return ran_maze.dfs_maze

def main(maze_method, speed=0.010, mode=0):
        """
        the main program of the program
        mode 0: default mode, build the wall
        mode 1: first all cell are wall, then pull down the wall
        """
        screen = pygame.display.set_mode(resolution, 0, 32)
        clock = pygame.time.Clock()
        maze, cell_list = maze_method()
        index = 0
        pass_time = 0
        grid_view = GridView(screen, width, height, grid_size, grid_line_color) 
        while True:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                exit()

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

                time_passed_seconds = clock.tick() / 1000.0
                pass_time += time_passed_seconds

                if pass_time >= speed:
                        pass_time = 0
                        if index + 1 < len(cell_list):
                                index += 1

                pygame.display.update()

if __name__ == '__main__':
        main(maze_method = get_maze_method(None), mode = 1)
                                        
