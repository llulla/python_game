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

#캐릭터(스프라이트) 불러오기
character= pygame.image.load("D:/study_2107/pygames/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width /2) - (character_width/2) #화면 가로 절반 크기에 해당
character_y_pos = screen_height - character_height#화면 세로 크기 가장 아래에 해당

#이동 좌표
to_x =0
to_y =0
# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=0.1
            elif event.key == pygame.K_RIGHT:
                to_x +=0.1
            elif event.key == pygame.K_UP:
                to_y -=0.1
            elif event.key == pygame.K_DOWN:
                to_y +=0.1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
    
    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos <0:
        character_y_pos =0
    elif character_y_pos > screen_height -  character_height:
        character_y_pos = screen_height - character_height
    # screen.fill((255,10,255))  #rgb 값으로 배경 그리기 
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기
# pygame 종료
pygame.quit()
