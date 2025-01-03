import pygame
import scheme

class Rect():
    def __init__(self, x, floor):
        self.x = x
        self.floor = floor
    
    def get_rect(self):
        if self.floor == 0:
            return pygame.Rect(self.x - 50, scheme.SIZE[1] - 50, 50, 50)
        elif self.floor == 1:
            return pygame.Rect(self.x - 50, scheme.SIZE[1] - 50 - 125, 50, 50 )
    
    def draw(self):
        pygame.draw.rect(scheme.screen, (134, 132, 156), self.get_rect())
    
    def is_collided_with_p(self, player_rect):
        if pygame.Rect.colliderect(player_rect, self.get_rect()):
            return True
        else:
            return False
        
        
class Levels():
    def _level_text(t):
        scheme.text(t, (100 , 900), 100, (scheme.WHITE))
    
    def get_level(level_num):
        if level_num == 1:
            rects = [Rect(900, 0)]
            return rects
        elif level_num == 2:
            rects = [Rect(500, 0), Rect(900, 0), Rect(1300, 0)]
            return rects
        elif level_num == 3:
            rects = [Rect(900, 0), Rect(925, 0), Rect(1200, 0), Rect(1225, 0)]
            return rects
        elif level_num == 4:
            rects = [Rect(900, 0), Rect(1125, 1), Rect(1350, 0)]
            return rects
        elif level_num == 5:
            rects = [Rect(900, 0), Rect(1125, 1), Rect(1350, 0), Rect(1575, 1), Rect(1800, 0)]
            return rects
        elif level_num == 6:
            rects = [Rect(900, 0), Rect(1100, 1), Rect(1300, 0)]
            return rects
        elif level_num == 7:
            rects = [Rect(900, 0), Rect(1075, 1), Rect(1250, 0)]
            return rects
        elif level_num == 8:
            rects = []
            return rects
        elif level_num == 9:
            rects = [Rect(900, 0), Rect(900, 1)]
            return rects
        elif level_num == 10:
            rects = []
            return rects
        elif level_num == 11:
            rects = [Rect(600, 0), Rect(800, 1), Rect(1000, 0), Rect(1200, 1), Rect(1400, 0), Rect(1600, 1), Rect(1800, 0)]
            return rects
            