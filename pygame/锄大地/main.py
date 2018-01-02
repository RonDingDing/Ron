import pygame
import os
import sys
import traceback
import card
import random
import function
from pygame.locals import *

pygame.init()
pygame.mixer.init()
bg_size =  width, height = 800, 600
bg =  pygame.image.load(os.path.join("image","bg.jpg")) 
bg_rect = bg.get_rect()
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("锄大地")
clock = pygame.time.Clock()
BLACK = (0,0,0)

#音效
pygame.mixer.music.load(os.path.join("music", random.choice(["background.ogg", "background1.ogg"])))
 
pygame.mixer.music.set_volume(0.2)

startingmusic = pygame.mixer.Sound(os.path.join("music", "start.ogg"))
winmusic = pygame.mixer.Sound(os.path.join("music", "wincc.ogg"))
zme = pygame.mixer.Sound(os.path.join("music", "zombify-male.ogg"))
zfe = pygame.mixer.Sound(os.path.join("music", "zombify-female.ogg"))

 
sima= [pygame.mixer.Sound(os.path.join("music", "sima"+str(i)+".ogg")) for i in range(4)]
simadeath  =  [pygame.mixer.Sound(os.path.join("music", "simadeath"+str(i)+".ogg")) for i in range(2)]
sunshangxiang  = [pygame.mixer.Sound(os.path.join("music", "sunshangxiang"+str(i)+".ogg") ) for i in range(3)]
zhangjiao = [pygame.mixer.Sound(os.path.join("music", "zhangjiao"+str(i)+".ogg") ) for i in range(6)]
liuli = [pygame.mixer.Sound(os.path.join("music", "liuli"+str(i)+".ogg") ) for i in range(4)]
 
sunshangxiangdeath = [pygame.mixer.Sound(os.path.join("music", "sunshangxiangdeath"+str(i)+".ogg")) for i in range(2)]
zhaoyun = [pygame.mixer.Sound(os.path.join("music", "zhaoyun"+str(i)+".ogg")) for i in range(6)]
zhaoyundeath = [pygame.mixer.Sound(os.path.join("music", "zhaoyundeath"+str(i)+".ogg")) for i in range(2)]



music = (sima+ simadeath+sunshangxiang+sunshangxiangdeath+zhaoyun+zhaoyundeath)
music.extend([startingmusic, winmusic])

for each in music:
    each.set_volume (0.4)
 


#出牌后X轴改变的情况 
class Button(pygame.sprite.Sprite):
    def __init__(self, bg_size, image,  position):   
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.width, self.height = bg_size[0], bg_size[1]
 

        
 
def main():
    # 手牌的框
    
    pygame.mixer.music.play(-1)
    kuang_wid, kuang_hgt = 400, 150
    card_wid, card_hgt = 112, 150

    # 已经出的框
    onkuang_wid, onkuang_hgt = 300, 150
         
    # 用来设置程序运行
    running =  True

    # 按钮初始化

    confirm_red = os.path.join("image", "confirm_red.png")
    confirm_reded = os.path.join("image", "confirm_red_down.png") 
    confirm_green = os.path.join("image","confirm_green.png")
    confirm_greened= os.path.join("image","confirm_green_down.png") 
    confirm_bg_size = confirm_wid, confirm_hgt = 67, 26
    confirm_position = (width - confirm_wid*3)//2, height  - card_hgt - confirm_hgt*2+15

    confirmer = Button(confirm_bg_size, confirm_red, confirm_position )  

    shu_image = os.path.join("image", "shu.png") 
    shu_bg_size = shu_wid, shu_hgt =  28, 28
    shu_position = (width -  shu_bg_size[0])//2, (height  - card_hgt - confirm_hgt*2+15)

    shu =  Button(shu_bg_size, shu_image , shu_position )  

    wu_image = os.path.join("image", "wu.png") 
    wu_bg_size = wu_wid, wu_hgt =  28, 28
    wu_position = (width -  wu_bg_size[0])//2, (height  - card_hgt - confirm_hgt*2+15)

    wu =  Button(wu_bg_size, wu_image, wu_position )

    wei_image = os.path.join("image", "wei.png") 
    wei_bg_size = wei_wid, wei_hgt =  28, 28
    wei_position = (width -  wei_bg_size[0])//2, (height  - card_hgt - confirm_hgt*2+15)

    wei =  Button(wei_bg_size, wei_image , wei_position )
    
    god_image = os.path.join("image", "god.png") 
    god_bg_size = god_wid, god_hgt =  28, 28
    god_position = (width -  god_bg_size[0])//2, (height  - card_hgt - confirm_hgt*2+15)

    god =  Button(god_bg_size, god_image, god_position )
    
    cancel_red = os.path.join("image", "cancel_red.png")
    cancel_reded= os.path.join("image", "cancel_red_down.png")
    cancel_green = os.path.join("image","cancel_green.png")
    cancel_greened = os.path.join("image","cancel_green_down.png") 
    cancel_bg_size = cancel_wid, cancel_hgt = 67, 26
    canceler_position = (width - confirm_wid*3)//2+ confirm_wid*2, height - card_hgt -  confirm_hgt*2+15

    canceler = Button(cancel_bg_size,  cancel_green, canceler_position)

     
    sortsuiter_image=  os.path.join("image", "sortsuit.png")
    sortsuiter_imageed = os.path.join("image", "sortsuit_down.png")
    sortsuit_bg_size= sortsuit_wid, sortsuit_hgt  = 65, 29
    sortsuit_position = sortsuit_posx,  sortsuit_posy = 50, height - sortsuit_wid

    sortsuiter = Button(sortsuit_bg_size, sortsuiter_image, sortsuit_position)

     
    sortnumber_image = os.path.join("image", "sortnumber.png")
    sortnumber_imageed = os.path.join("image", "sortnumber_down.png") 
    sortnumber_bg_size=sortnumber_wid, sortnumber_hgt = 65, 29
    sortnumber_position = sortnumber_posx,  sortnumber_posy = width - 50 -  sortnumber_wid, height - sortnumber_wid

    sortnumberer = Button(sortnumber_bg_size , sortnumber_image, sortnumber_position)
    
    # 牌堆精灵组
    pilelist= card.pile
    random.shuffle(pilelist)
    
    #用来设置派牌
    paipai = False

        #ondesk位置
    x = width//2
    b =12
    w1 = [x]
    w2 = [x-b, x+b]
    w3 = [x-2*b, x, x+2*b]
    w4 = [x-3*b, x-b, x+b, x+3*b]
    w5 = [x-4*b, x-2*b, x, x+2*b, x+4*b]
    w6 = [x-5*b, x-3*b, x-b, x+b, x+3*b, x+5*b]
    w7 = [x-6*b, x-4*b, x-2*b, x, x+2*b, x+4*b, x+6*b]
    w8 = [x-7*b, x-5*b, x-3*b, x-b, x+b, x+3*b, x+5*b, x+7*b]
    w9 = [x-8*b, x-6*b, x-4*b, x-2*b, x, x+2*b, x+4*b, x+6*b, x+8*b]
    w10 = [x-9*b, x-7*b, x-5*b, x-3*b, x-b, x+b, x+3*b, x+5*b, x+7*b, x+9*b]
    w11 = [x-10*b, x-8*b, x-6*b, x-4*b, x-2*b, x, x+2*b, x+4*b, x+6*b, x+8*b, x+10*b]
    w12 = [x-11*b, x-9*b, x-7*b, x-5*b, x-3*b, x-b, x+b, x+3*b, x+5*b, x+7*b, x+9*b, x+11*b]
    w13 = [x-12*b, x-10*b, x-8*b, x-6*b, x-4*b, x-2*b, x, x+2*b, x+4*b, x+6*b, x+8*b, x+10*b, x+12*b]
 

    
    w = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13]

    y= height//2
    a =12
    h1 = [y]
    h2 = [y-a, y+a]
    h3 = [y-2*a, y, y+2*a]
    h4 = [y-3*a, y-a, y+a, y+3*a]
    h5 = [y-4*a, y-2*a, y, y+2*a, y+4*a]
    h6 = [y-5*a, y-3*a, y-a, y+a, y+3*a, y+5*a]
    h7 = [y-6*a, y-4*a, y-2*a, y, y+2*a, y+4*a, y+6*a]
    h8 = [y-7*a, y-5*a, y-3*a, y-a, y+a, y+3*a, y+5*a, y+7*a]
    h9 = [y-8*a, y-6*a, y-4*a, y-2*a, y, y+2*a, y+4*a, y+6*a, y+8*a]
    h10 = [y-9*a, y-7*a, y-5*a, y-3*a, y-a, y+a, y+3*a, y+5*a, y+7*a, y+9*a]
    h11 = [y-10*a, y-8*a, y-6*a, y-4*a, y-2*a, y, y+2*a, y+4*a, y+6*a, y+8*a, y+10*a]
    h12 = [y-11*a, y-9*a, y-7*a, y-5*a, y-3*a, y-a, y+a, y+3*a, y+5*a, y+7*a, y+9*a, y+11*a]
    h13 = [y-12*a, y-10*a, y-8*a, y-6*a, y-4*a, y-2*a, y, y+2*a, y+4*a, y+6*a, y+8*a, y+10*a, y+12*a]
    h = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13] 
    
    posy1 = height - card_hgt//2 - 10
    posy2 = 85
    posx1 = 60
    posx2 = width - card_wid//2 -10
      
    startpos = []
 

    #设置四个player手牌的初始位置
    for i in range(13):
        startpos.append((w13[i], posy1))
        startpos.append((posx2, h13[i]))
        startpos.append((w13[i], posy2))
        startpos.append((posx1, h13[i]))


    #初始化四个Player和ondesk
    player0 = []
    player1 = []
    player2 = []
    player3 = []
    playerlist =  [player0 , player1, player2,  player3]
    players = [0,1,2,3]
    currentplayer = 5
    oldplayers = [None,] *4
    oldplayerlist = [None,] *4


 
    #局面变量
    ondesk = []
    selected = []
    selectc1 = []
    selectc2 = []
    selectc3 = []  
   
    started = False
    canplay = False
    canpass = True
    canplayc1 = False
    canplayc2 = False
    canplayc3 = False
    discard = []
     
    playedsituation = [5, 5, 5, 5]
    pass_font = pygame.font.Font("font/font.ttf", 20)
    paused = False
    #用于切换
    PAUSETIME = USEREVENT
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == USEREVENT:
                paused = False
                pygame.time.set_timer(PAUSETIME, 0)
            screen.blit(bg, (0,0))
            

            #未派牌，就派牌
            if paipai == False:                           
                for e in range(52):
                    screen.blit(pilelist[e].image, pilelist[e].rect)
                    
                if event.type == MOUSEBUTTONDOWN:
                    startingmusic.play()
                    if event.button == 1 and bg_rect.collidepoint(event.pos):
                        for e in range(52):                            
                            pilelist[e].rect.center = startpos[e]
                            screen.blit(pilelist[e].image, pilelist[e].rect)                            
                            playerlist[e%4].append(pilelist[e])                            
                            pygame.display.update()
                        paused = True
                        pygame.time.set_timer(PAUSETIME, 3000)
                        
                       
                        
                    
                    paipai = True

            #派牌了player0就要露出手牌了
            elif paipai == True:
 
                if canplay and currentplayer %4 ==0:
                    confirmer.image = pygame.image.load(confirm_green)
                    screen.blit(confirmer.image, confirmer.rect)
                    
                elif not canplay:
                    confirmer.image = pygame.image.load(confirm_red)
                    screen.blit(confirmer.image, confirmer.rect)

                
    
                if not player1 or not player2 or not player3 or not player0:
                    pygame.mixer.pause()
                    
                    if not player1:
                        pygame.mixer.unpause()
                        random.choice(zhaoyundeath).play()
                    if not player2:
                        pygame.mixer.unpause()
                        random.choice(sunshangxiangdeath).play()
                    if not player3:
                        pygame.mixer.unpause()
                        random.choice(simadeath).play()
                    if not player0:
                        winmusic.play()
                    
                    aba, bbb, cbc, dbd = len(player0),  len(player1),  len(player2),  len(player3)
                    for each in  aba, bbb, cbc, dbd:
                        if 8<= each <= 10:
                            each +=each 
                        elif 11<= each <= 12:
                            each +=each *2
                        elif each == 13:
                            each == 52
                    data = str("你："+str(aba)+"  赵云："+str(bbb)+"  孙尚香："+str(cbc)+"  司马懿："+str(dbd))
                    with open ("record.txt", "w") as f:
                        pass
                    with open ("record.txt", "a") as f:
                        f.writelines(data)
                    
                            
                    
                        
                    pygame.time.delay(10000)
                    pygame.quit()
                    sys.exit()
                    
                
               
      
                #转换图片
                for e in player0:
                    e.image = pygame.image.load(os.path.join("image", str(e.rank)+".jpg"))
                for e in player3:
                    e.image = pygame.image.load(os.path.join("image", "blant.png")).convert_alpha()
                for e in player2:
                    e.image = pygame.image.load(os.path.join("image", "blank.png")).convert_alpha()
                for e in player1:
                    e.image = pygame.image.load(os.path.join("image", "blang.png")).convert_alpha()
                for e in ondesk:
                    e.image = pygame.image.load(os.path.join("image", str(e.rank)+".jpg")).convert()
                 #绘制桌上的牌
                if ondesk:
                    for each in ondesk:
                        screen.blit(each.image, each.rect)
                #绘制牌   
                for i in range(len(player0)):
                    screen.blit(player0[i].image, player0[i].rect)
                for i in range(len(player1)):
                    screen.blit(player1[i].image, player1[i].rect)
                for i in range(len(player2)):  
                    screen.blit(player2[i].image, player2[i].rect)
                for i in range(len(player3)):
                    screen.blit(player3[i].image, player3[i].rect)
                #绘制按钮                       
                screen.blit(confirmer.image, confirmer.rect)
                screen.blit(canceler.image, canceler.rect)
                screen.blit(sortsuiter.image, sortsuiter.rect)
                screen.blit(sortnumberer.image, sortnumberer.rect)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                pygame.display.update()

                
                #AI主循环
                    #####
                #第一次出牌
                if not paused:
                    if started == False: 
                        if card.diamond3 in player0:
                           
                            currentplayer = 0                            
                            screen.blit(god.image, god.rect)
                       
                      
                                
                        elif card.diamond3 in player1:
                         
                            
                            pygame.time.set_timer(PAUSETIME, 3000)
                            random.choice(zhaoyun).play()
                            screen.blit(shu.image, (width - 20 - card_hgt - shu_wid, (height- shu_hgt)//2 ))
                            currentplayer = 1
                            paused = True 
                            pygame.display.update()
                            oldplayer1 = player1.copy() 
                            player1, selectc1, ondesk,  canplayc1, started, currentplayer, discard, playedsituation = \
                                          function.turn_ai (player1, selectc1, ondesk,  canplayc1, started, currentplayer, discard, w, height, screen, playedsituation)   
                            player1 = function.afterplay1(oldplayer1, player1, h, card_wid)
                            started = True   
                            currentplayer+=1
                            
               
                             
                            
                        elif card.diamond3 in player2:
                      
                            currentplayer = 2
                            
                            random.choice(sunshangxiang).play()
                            screen.blit(wu.image, ((width - wu_wid)//2, 20 + card_hgt))
                            paused = True
                            pygame.time.set_timer(PAUSETIME, 3000)
                            pygame.display.update()
                            oldplayer2 = player2.copy() 
                            player2, selectc2, ondesk,  canplayc2, started, currentplayer, discard, playedsituation = \
                                          function.turn_ai (player2, selectc2, ondesk,  canplayc2, started, currentplayer, discard, w, height, screen, playedsituation)   
                            player2 = function.afterplay2(oldplayer2, player2, w, card_hgt)
                            started = True   
                            currentplayer+=1
                            
                     
                        
                             
                            
                        elif card.diamond3 in player3:
              
                            currentplayer = 3
                  
                            random.choice(sima).play()
                            screen.blit(wei.image, (20 + card_wid,  (height - wei_hgt)//2))
                            paused = True
                            pygame.time.set_timer(PAUSETIME, 3000)
                            pygame.display.update()
                            oldplayer3 = player3.copy()                            
                            player3, selectc3, ondesk,  canplayc3, started, currentplayer, discard, playedsituation = \
                                          function.turn_ai (player3, selectc3, ondesk,  canplayc3, started, currentplayer, discard, w, height, screen, playedsituation)   
                            player3 = function.afterplay3(oldplayer3, player3, h, card_wid)
                            started = True   
                            currentplayer+=1
                            
            
                      
                           

                        
                        
                    elif started == True:
                        currentplayer = currentplayer % 4
                        
                        if currentplayer %4 == 0:
   
                            screen.blit(god.image, god.rect)
                             
                            if playedsituation ==[1, 0, 0, 0]:
                            
                                ondesk.clear()
                                canpass = False
                                playedsituation == [5,5,5,5]
                                
                                   
                 
                                
                        elif currentplayer %4 == 1:
                     
                            random.choice(zhaoyun).play()
                            screen.blit(shu.image, ( width - 20 - card_wid - shu_wid, (height- shu_hgt)//2 ))
                            
                            
                            paused = True
                            pygame.time.set_timer(PAUSETIME, 3000)
                            pygame.display.update()
                            oldplayer1 = player1.copy()
                            player1, selectc1, ondesk,  canplayc1, started, currentplayer, discard, playedsituation =\
                                     function.turn_ai(player1, selectc1, ondesk,  canplayc1, started, currentplayer, discard, w, height, screen, playedsituation)
                            player1 = function.afterplay1(oldplayer1, player1, h, card_wid)
                            currentplayer+=1
                            
           
                           
                            
                        elif currentplayer %4 == 2:
                   
                            random.choice(sunshangxiang).play()
                            screen.blit(wu.image, ((width - wu_wid)//2, 20 + card_hgt))
                            
                            
                            paused = True
                            pygame.time.set_timer(PAUSETIME, 3000)
                            pygame.display.update()
                            oldplayer2 = player2.copy()
                            player2, selectc2, ondesk,  canplayc2, started, currentplayer, discard, playedsituation =\
                                     function.turn_ai(player2, selectc2, ondesk,  canplayc2, started, currentplayer, discard, w, height, screen, playedsituation)
                             
                            player2 = function.afterplay2(oldplayer2, player2, w, card_hgt)
                            currentplayer+=1
                            
  
 
                                    
                        elif currentplayer %4 == 3:
                      
                            random.choice(sima).play()
                            screen.blit(wei.image, (20 + card_wid,  (height - wei_hgt)//2))
                            
                            paused = True
                            pygame.time.set_timer(PAUSETIME, 3000)
                            
                            pygame.display.update()
                            
                            oldplayer3 = player3.copy()
                            player3, selectc3, ondesk,  canplayc3, started, currentplayer, discard, playedsituation =\
                                     function.turn_ai(player3, selectc3, ondesk,  canplayc3, started, currentplayer, discard, w, height, screen, playedsituation)

                            
                            player3 = function.afterplay3(oldplayer3, player3, h, card_wid)
                            currentplayer+=1
                            
 
     
                       
                                    
                       

                        
                    #检测点击
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if sortnumberer.rect.collidepoint(event.pos):
                                sortnumberer.image = pygame.image.load(sortnumber_imageed)
                                zme.play()
                                
                                pygame.display.update()
                                function.sortingnumber(player0)
                                function.sortingnumberee(player1)
                                function.sortingnumber(player2)
                                function.sortingnumberee(player3)
     
                                    
                            elif sortsuiter.rect.collidepoint(event.pos):
                                sortsuiter.image = pygame.image.load(sortsuiter_imageed)
                                zfe.play()
                                pygame.display.update()
                                player0 = function.sortingsuit(player0)
                                player1 = function.sortingsuitee(player1)
                                player2 = function.sortingsuit(player2)
                                player3 = function.sortingsuitee(player3)     
                               
     
                                    
                            elif confirmer.rect.collidepoint(event.pos):
                               
                                    
                                if canplay and selected and currentplayer %4 ==0:
                                    started = True
                                    random.choice(zhangjiao).play()
                                    confirmer.image = pygame.image.load(confirm_green)
                                    pygame.display.update()
                                    oldplayer0 = player0.copy()
                                    player0, selected, ondesk, discard = function.play(player0, selected, ondesk, discard, w, height, screen)
                                    player0 = function.afterplay0(oldplayer0, player0, w, card_hgt)
                                    playedsituation[0] =1 
                                    currentplayer+=1
                                    started = True   
                                    paused = True
                                    canpass = True
                                    pygame.time.set_timer(PAUSETIME, 3000)
                                    
                                selected.clear()
                                
                                tops = [each.rect.top for each in player0]
                                for each in player0:
                                    each.chosen = False
                                    each.rect.top = max(tops)
                                     
                            elif canceler.rect.collidepoint(event.pos):
                                if canpass == True:
                                    selected.clear()
                                    tops = [each.rect.top for each in player0]
                                    for each in player0:
                                        each.chosen = False
                                        each.rect.top = max(tops)
                                    
                                    if currentplayer %4 ==0 and started == True:
                                         random.choice(liuli).play()
                                         canceler.image = pygame.image.load(cancel_red)
                                         pygame.display.update()
                                         playedsituation[0] =0 
                                         currentplayer+=1
                                         paused = True
                                         pygame.time.set_timer(PAUSETIME, 3000)

                        
                                   
                            confirmer.image = pygame.image.load(confirm_red)
                            pygame.display.update()
                             
                        for i in range(len(player0)):
                            if player0[i-1].rect.top < mouse_y <player0[i-1].rect.bottom:
                                if i < len(player0) -1 :
                                    if player0[i].rect.left < mouse_x <player0[i+1].rect.left:                                
                                        if event.button == 1:
                                            if not player0[i].chosen:                                            
                                                selected.append(player0[i])
                                                player0[i].rect.top -= 10
                                                player0[i].chosen = True
                                                canplay  = function.ifcanplay(selected, ondesk, canplay, started)
                                                if started == False:
                                                    if card.diamond3 not in selected:
                                                        canplay = False
                                                pygame.display.update()
                                                                                          
      
                                                    
                                            elif player0[i].chosen:
                                                selected.remove(player0[i])
                                                player0[i].rect.top += 10                             
                                                player0[i].chosen = False
                                                canplay = function.ifcanplay(selected, ondesk, canplay, started)
                                                if started == False:
                                                    if card.diamond3 not in selected:
                                                        canplay = False
                                                pygame.display.update()
                                                               
                                elif i == len(player0) -1:
                                    if player0[i].rect.left < mouse_x <player0[i].rect.right:                                
                                        if event.button == 1:
                                            if not player0[i].chosen:                                            
                                                player0[i].rect.top -= 10                             
                                                player0[i].chosen = True
                                                selected.append(player0[i])
                                                canplay = function.ifcanplay(selected, ondesk,  canplay, started)
                                                if started == False:
                                                    if card.diamond3 not in selected:
                                                        canplay = False
                                                  
                                                
                                            elif player0[i].chosen:
                                                player0[i].rect.top += 10                             
                                                player0[i].chosen = False
                                                selected.remove(player0[i])
                                                canplay = function.ifcanplay(selected, ondesk,  canplay, started)
                                                if started == False:
                                                    if card.diamond3 not in selected:
                                                        canplay = False

                    elif event.type == MOUSEBUTTONUP:
                        if event.button == 1:
                            if sortnumberer.rect.collidepoint(event.pos):
                                sortnumberer.image = pygame.image.load(sortnumber_image)
                                pygame.display.update()
                            elif sortsuiter.rect.collidepoint(event.pos):
                                sortsuiter.image = pygame.image.load(sortsuiter_image)
                                pygame.display.update()
                            elif confirmer.rect.collidepoint(event.pos):
                                confirmer.image = pygame.image.load(confirm_red)
                                pygame.display.update()
                            elif canceler.rect.collidepoint(event.pos):
                                canceler.image = pygame.image.load(cancel_red)
                                pygame.display.update()
                                                                     
                        
            

             
                
 
        pygame.display.flip()
        clock.tick(200)
        

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
