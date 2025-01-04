import pygame
import scheme
pygame.init()

class Rect():
    def __init__(self, x, floor):
        self.x = x
        self.floor = floor
    
    def get_rect(self):
        if self.floor == 0:
            return pygame.Rect(self.x - 20, scheme.SIZE[1] - 20, 20, 20)
        elif self.floor == 1:
            return pygame.Rect(self.x - 20, scheme.SIZE[1] - 20 - 50, 20, 20)
    
    def draw(self):
        pygame.draw.rect(scheme.screen, (134, 132, 156), self.get_rect())
    
    def is_collided_with_p(self, player_rect):
        if pygame.Rect.colliderect(player_rect, self.get_rect()):
            return True
        else:
            return False
        
        
class Levels():
    def _level_text(t):
        scheme.text(t, (100 , 360), 20, (scheme.WHITE))
    
    def get_level(level_num):
        if level_num == 1:
            rects = [Rect(360, 0)]
        elif level_num == 2:
            rects = [Rect(200, 0), Rect(360, 0), Rect(520, 0)]
        elif level_num == 3:
            rects = [Rect(360, 0), Rect(370, 0), Rect(480, 0), Rect(490, 0)]
        elif level_num == 4:
            rects = [Rect(360, 0), Rect(450, 1), Rect(540, 0)]
        elif level_num == 5:
            rects = [Rect(360, 0), Rect(450, 1), Rect(540, 0), Rect(630, 1), Rect(720, 0)]
        elif level_num == 6:
            rects = [Rect(360, 0), Rect(440, 1), Rect(520, 0)]
        elif level_num == 7:
            rects = [Rect(360, 0), Rect(430, 1), Rect(500, 0)]
        elif level_num == 8:
            rects = []
        elif level_num == 9:
            rects = [Rect(360, 0), Rect(360, 1)]
        elif level_num == 10:
            rects = []
        elif level_num == 11:
            rects = [Rect(240, 0), Rect(320, 1), Rect(400, 0), Rect(480, 1), Rect(560, 0), Rect(640, 1), Rect(720, 0)]
        elif level_num == 12:
            rects = [Rect(320, 1)]
        elif level_num == 13:
            rects = []
        return rects
     