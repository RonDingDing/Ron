import pygame
import sys

# 初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255) # RGB

# 创建指定大小的窗口 Surface
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

# 加在图片
turtle = pygame.image.load("image/turtle.png")
# 获得图像的位置矩形
position = turtle.get_rect()

# 先定义向左向右走时龟头朝向
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #控制移动图像
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-1, 0]
                turtle = l_head          # 左右翻转乌龟
            if event.key == pygame.K_RIGHT:
                speed = [1, 0]
                turtle = r_head          # 左右翻转乌龟
            if event.key == pygame.K_UP:
                speed = [0, -1]
            if event.key == pygame.K_DOWN:
                speed = [0, 1]
        if event.type == pygame.KEYUP:
            speed = [-2, 1]
            
    # 自动移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position)
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    # pygame.time.delay(10)
