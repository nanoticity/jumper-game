import pygame
import pygame.mixer
import levels
import scheme
import asyncio

pygame.init()
pygame.mixer.init(22050, -16, 2, 2048)

if __name__ == "__main__":
    song = pygame.mixer.music.load("jumper-game.mp3")
else:
    song = pygame.mixer.music.load("/lib/python3.12/site-packages/jumper_game/jumper-game.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)

def text(text, pos, size, color):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    textpos = text.get_rect(x = pos[0], y = pos[1])
    scheme.screen.blit(text, textpos)

def level_text(t):
    text(t, (40 , 400), 40, (scheme.WHITE))

async def main():
    scheme.screen = pygame.display.set_mode(scheme.SIZE) 
    pygame.display.set_caption("Space: Jump!")

    prect = pygame.Rect(0, scheme.SIZE[1] - 40, 40, 40)
    vel = 6

    is_jump = False
    jump_count = 7
    frames = 0
    set = False
    old_found = False
    paused = False
    penalty_start = 0

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
                elif e.key == pygame.K_r:
                    level = 1
                    offset += time
                elif e.key == pygame.K_e:
                    help = not help
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    is_jump = True
       
        if paused:
            if penalty_start + 500 < pygame.time.get_ticks():
                paused = False
                prect.x = 0
        else:
            prect.x += vel

        if is_jump and not paused:
            if not old_found:
                old_jump_count = jump_count
                old_found = True
            multiplier = 0.4
            if jump_count >= -7:
                if jump_count < 0:
                    neg = -1
                else:
                    neg = 1
                
                prect.y -= (jump_count ** 2) * multiplier * neg
                jump_count -= 1
            else:
                is_jump = False
                prect.y = scheme.SIZE[1] - prect.width
                jump_count = old_jump_count
                old_found = False

        if prect.x > scheme.SIZE[0] - prect.width:
            prect.x = 0
            level += 1
            set = False
        time = round((pygame.time.get_ticks() / 1000) - offset, 3)
        scheme.screen.fill(scheme.DARK_BLUE)
        
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
                jump_count = 8
                set = True
            rects = levels.Levels.get_level(level)
            level_text("Now jump?")
        elif level == 10:
            rects = levels.Levels.get_level(level)
            level_text("Now that was interesting.")
        elif level == 11:
            if not set:
                jump_count = 7
                set = True
            rects = levels.Levels.get_level(level)
            level_text("Now it's getting serious.")
        elif level == 12:
            level_text("haha")
            rects = levels.Levels.get_level(level)
        elif level == 13:
            level_text("btw u have 0 pixels to spare")
            rects = levels.Levels.get_level(level)
        elif level == 14:
            level_text("bye bye")
            rects = levels.Levels.get_level(level)
        elif level == 15:
            level = 1
            offset += time
            
        for rect in rects:
            rect.draw()
            if rect.is_collided_with_p(prect):
                if not paused:
                    penalty_start = pygame.time.get_ticks()
                paused = True
        
        fps = frames / (pygame.time.get_ticks() / 1000)
        text("Level " + str(level), (50, 50), 50, scheme.WHITE)
        text("Time: " + str(time), (50, 100), 50, scheme.WHITE)
        text("FPS: " + "{:.2f}".format(fps), (650, 50), 30, scheme.WHITE)
        pygame.draw.rect(scheme.screen, (134, 132, 156), prect)
        pygame.display.update()
        if not help:
            await asyncio.sleep(0.02)
        elif help:
            await asyncio.sleep(0.1)
        frames += 1

    

if __name__ == "__main__":
    asyncio.run(main())