import pygame

pygame.init() #초기화 반드시 해줘야함

#화면 크기 설정
screen_width = 480  #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#배경 이미지 가져오기
background = pygame.image.load("D:/study_2107/pygames/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,10,255))  #rgb 값
    #screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() # 게임화면 다시 그리기
# pygame 종료
pygame.quit()
