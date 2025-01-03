import pygame
import levels
import scheme

pygame.init()

SIZE = [1800, 1035]

DARK_BLUE = (34, 32, 56)
WHITE = (255, 255, 255)

prect = pygame.Rect(0, scheme.SIZE[1] - 100, 100, 100)

game_over = False

vel = 12

def text(text, pos, size, color):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    textpos = text.get_rect(x = pos[0], y = pos[1])
    scheme.screen.blit(text, textpos)

def level_text(t):
    text(t, (100 , 900), 100, (scheme.WHITE))

is_jump = False
jump_count = 10
set = False
old_found = False
dh = False

level = 1
rects = []
offset = 0
help = False

clock = pygame.time.Clock()
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            elif not is_jump and e.key == pygame.K_SPACE:
                is_jump = True
            elif e.key == pygame.K_d:
                dh = not dh
            elif e.key == pygame.K_r:
                level = 1
                offset += time
            elif e.key == pygame.K_e:
                help = not help
    prect.x += vel
    if dh:
        prect.y = 0
    if is_jump:
        if not old_found:
            old_jump_count = jump_count
            old_found = True
        multiplier = 0.4
        if jump_count >= -10:
            if jump_count < 0:
                neg = -1
            else:
                neg = 1
            prect.y -= (jump_count ** 2) * multiplier * neg
            jump_count -= 1
        else:
            is_jump = False
            prect.y = SIZE[1] - prect.width
            jump_count = old_jump_count
            old_found = False

    if prect.x > scheme.SIZE[0] - prect.width:
        prect.x = 0
        level += 1
        set = False
    time = round((pygame.time.get_ticks() / 1000) - offset, 3)
    scheme.screen.fill(scheme.DARK_BLUE)
    """
    9 
    if not set:
            jump_count = 13
            set = True
            
            
    12
    if not set:
            jump_count = 10
            set = True
    
    """
    if level == 1:
        level_text("Easy right?")
        rects = levels.Levels.get_level(level)
    elif level == 2:
        level_text("Now there's multiple!")
        rects = levels.Levels.get_level(level)
    elif level == 3:
        level_text("Now their longer! (75 pixels for the nerds)")
        rects = levels.Levels.get_level(level)
    elif level == 4:
        level_text("Now your can't jump when you're below a block.")
        rects = levels.Levels.get_level(level)
    elif level == 5:
        level_text("Now it's longer.")
        rects = levels.Levels.get_level(level)
    elif level == 6:
        level_text("Now the gap is smaller.")
        rects = levels.Levels.get_level(level)
    elif level == 7:
        level_text("Even smaller :D")
        rects = levels.Levels.get_level(level)
    elif level == 8:
        level_text("Let's give you a little break")
        rects = levels.Levels.get_level(level)
    elif level == 9:
        if not set:
            jump_count = 13
            set = True
        rects = levels.Levels.get_level(level)
        level_text("Now jump?")
    elif level == 11:
        rects = levels.Levels.get_level(level)
        level_text("Now that was interesting.")
    elif level == 12:
        rects = levels.Levels.get_level(level)
        if not set:
            jump_count = 8
            set = True
        level_text("Now it's getting serious.")
        
    elif level == 13:
        with open("times.txt", "a") as times:
            times.write(str(pygame.time.get_ticks() / 1000) + "\n")
        level = 1
        offset += time
        
    for rect in rects:
        rect.draw()
        if rect.is_collided_with_p(prect):
            prect.x = 0
            pygame.time.wait(500)
    
    text("Level " + str(level), (50, 50), 50, scheme.WHITE)
    text("Time: " + str(time), (50, 100), 50, scheme.WHITE)
    pygame.draw.rect(scheme.screen, (134, 132, 156), prect)
    pygame.display.update()
    if not help:
        clock.tick(60)
    elif help:
        clock.tick(8)
    