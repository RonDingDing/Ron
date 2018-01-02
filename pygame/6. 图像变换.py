import pygame
import sys
from pygame.locals import *

# 初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [5, 0]
bg = (255, 255, 255) # RGB

fullscreen = False

# 创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size, RESIZABLE)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")


# 设置放大缩小的比率
ratio = 1.0

oturtle = pygame.image.load("image/turtle.png")
turtle = oturtle
oturtle_rect = oturtle.get_rect()
position =  oturtle_rect
turtle_rect = oturtle_rect
turtle_center = position.center

a = position.right
b = position.bottom

left_head = turtle
right_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         

            
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                 
                speed = [-5, 0]
            if event.key == K_RIGHT:
                 
                speed = [5, 0]
            if event.key == K_UP:
                speed = [0, -5]
            if event.key == K_DOWN:
                speed = [0, 5]

            # 全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1024, 768), FULLSCREEN | HWSURFACE)
                    width, height = 1024, 768
                else:
                    screen = pygame.display.set_mode(size)

            # 放大、缩小小乌龟（=、-），空格键恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                
                # 最大只能放大一倍，缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0

                turtle = pygame.transform.smoothscale(oturtle, \
                                             (int(oturtle_rect.width * ratio), \
                                             int(oturtle_rect.height * ratio)))
                
                
                right_head = pygame.transform.flip(turtle, True, False)
                left_head = turtle
                 
                position = turtle.get_rect(center = position.center)

                c = turtle_center[0]
                d = turtle_center[1]
                
                if turtle_center[0] + (a*ratio/2) > width:
                    c = width - (a*ratio/2)                
                    position.center = (c,d)
                if turtle_center[1] + (b*ratio/2) > height:                    
                    d = height - (b*ratio/2)
                    position.center = (c,d)

                 
                 

                                  
                
                 
                
                
            
            

                
       
        
                
        # 用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)
            
            position = turtle.get_rect(center = turtle_center)
                             
                
                
                   
                
                
            if position.right > width:
                position.right = width
            if position.bottom > height:
                position.bottom = height
                    
            
            
            

    # 移动图像
    position = position.move(speed)
    turtle_center = (turtle_center[0]+speed[0], turtle_center[1]+speed[1] ) 

    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = left_head
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    if speed[0] > 0:
        turtle = right_head
    elif speed[0] < 0:
        turtle = left_head
        
        

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10)
