import pygame
import time
qq = 0
cc = 0
wwww = 0#ssssssssssssssss
pygame.init()
screen = pygame.display.set_mode([800,600])
#xxxx = input("cd:")
timer = pygame.time.Clock()
if False:#xxxx != "7271111111":
    cc = 1
    # print("cd is error!")
    # pygame.quit()
else:
    cai_ji = pygame.image.load("cai_ji.png")
    screen.blit(cai_ji,(1,1))
    pygame.display.update()
    #time.sleep(1)
    finder = pygame.image.load("finder.png")
    BLACK = (0,0,0)
    screen.fill(BLACK)
    screen.blit(finder,(1,1))
    pygame.display.update()
    while(True):
        screen.blit(finder, (1, 1))
        xxxx = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        font = pygame.font.SysFont("Times",15)
        text = font.render(xxxx,True,BLACK)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 5
        screen.blit(text,text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wwww = 1
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                we_gi = event.pos
                #print("get event: " + str(event.pos))
                if we_gi[0] >= 0 and we_gi[0] <= 25 and we_gi[1] >= 565  and we_gi[1] <= 600:
                    wwww = 1
                elif we_gi[0] >= 25 and we_gi[0] <= 105 and we_gi[1] >= 565 and we_gi[1] <= 600:
                    qq = 1
            #elif event.type ==
        if wwww == 1:
            pygame.quit()
            break
        elif qq == 1:
            start = pygame.image.load("start.png")
            screen.blit(start, (1, 200))
            if we_gi[0] >= 0 and we_gi[0] <= 225 and we_gi[1] >= 250 and we_gi[1] <= 300:
                qq = 0
        pygame.display.update()
        timer.tick(8)