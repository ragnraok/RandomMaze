#A Gridview Class

import pygame
from pygame.locals import *

class GridView(object):
        """
        A Gridview Class
        """
        def __init__(self, surface, width, height, grid_size, grid_color, grid_width=1):
                """ initalize the grid view
                x_grid_num: the horizontal grid number(width/grid_size)
                y_grid_num: the vertical grid number(heigth/grid_size)
                """
                if width % grid_size != 0 or height % grid_size !=0:
                        raise CanNotDivideException('the grid_size is not suitable for width and height')

                self.x_grid_num = width / grid_size
                self.y_grid_num = height / grid_size

                self.surface = surface
                self.width = width
                self.height = height
                self.grid_size = grid_size
                self.grid_color = grid_color
                self.grid_width = grid_width

        def draw(self):
                """
                draw the grid
                """
                for y in range(0, self.height, self.grid_size):
                        for x in range(0, self.width, self.grid_size):
                                pygame.draw.rect(self.surface, self.grid_color, 
                                                 ((x, y), (self.grid_size, self.grid_size)), self.grid_width)

        def fill_a_cell(self, x, y, color):
                """
                fill a cell in the grid view
                x, y: the coordinate in the grid_view
                x: the column number
                y: the row number
                """
                if x > self.x_grid_num or y > self.y_grid_num or x < 0 or y < 0:
                        raise CoordinateTooBigException('the x y coordinate is error')
                
                pygame.draw.rect(self.surface, color, ((x*self.grid_size, y*self.grid_size), 
                                                       (self.grid_size, self.grid_size)), 0)

        def fill_a_cell_with_circle(self, x, y, color):
                """
                fill a cell with circle in the grid
                x, y: the coordinate in the grid_view
                x: the column number
                y: the row number
                """
                if x > self.x_grid_num or y > self.y_grid_num or x < 0 or y < 0:
                        raise CoordinateTooBigException('the x y coordinate is error')

                delta = self.grid_size // 2
                pygame.draw.circle(self.surface, color, (x*self.grid_size + delta, y*self.grid_size + delta),
                                   delta - 2, 0)




class CoordinateTooBigException(BaseException):
        def __init__(self, description):
                self.description = description

        def __unicode__(self):
                return 'error: ' + str(self.description)

class CanNotDivideException(BaseException):
        def __init__(self, description):
                self.description = description

        def __repr__(self):
                return 'error: ' + str(description)

        def __unicode__(self):
                return self.__repr__()

