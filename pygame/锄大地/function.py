import random, pygame, card, main, os
screen = main.screen

def ifcanplay(select, ondesk, canplay, started):
    selectc = select.copy()
    canplay = False
    lenc, maxc, levelc, matchrulec = 0, 0, 0, 0
    leno, maxo, levelo, matchruleo = 0, 0, 0, 0
    
    if selectc:
        lenc, maxc, levelc, matchrulec  = findpara_cardlist(selectc)
        if ondesk:
            leno, maxo, levelo, matchruleo = findpara_cardlist(ondesk)
            if matchrulec:
                if lenc == leno:
                    if lenc == 5:
                        if levelc > levelo:
                            canplay = True
                        elif levelc == levelo:
                            if maxc > maxo:
                                canplay = True 
                        elif levelc < levelo:
                            canplay = False
                    elif lenc == 1 or 2 or 3 or 4:
                        if maxc > maxo:
                            canplay = True
                    
            else:
                canplay = False
        elif not ondesk or not started:
            if matchrulec:
                canplay = True
 
        else:
            canplay = False


    if started == False:
        if card.diamond3 not in selectc:
            canplay = False
    
                  
                
    return canplay 



def sortingnumberifcanplay(cardlist):
 
    if cardlist:
 
        #开始20次循环排列
        for s in range(20):
            for i in range(len(cardlist)-1):
                if cardlist[i].rank < cardlist[i+1].rank:
                    cardlist[i], cardlist[i+1] = cardlist[i+1], cardlist[i]
                    
        #用新的cardlist重载cardlist，将所有的左坐标贴上，然后重新显示  
        
        return cardlist

def findpara_cardlist(cardlist):
    if cardlist:          
        matchrule = False
        leng = len(cardlist)        
        level = 0
        cardlist = sortingnumberifcanplay(cardlist)
        maxr = 0
 
        shunzi = False
        hua = False
        
        if leng ==1:
            matchrule = True
            maxr = cardlist[0].rank
            
        elif leng == 2:
            if cardlist[1].number == cardlist[0].number:
                matchrule = True
                maxr = cardlist[0].rank

        elif leng == 3:
            if cardlist[2].number == cardlist[1].number == cardlist[0].number:
                matchrule = True
                maxr = cardlist[0].rank

        elif leng == 4:
            if cardlist[3].number == cardlist[2].number == cardlist[1].number == cardlist[0].number:
                matchrule = True
                maxr = cardlist[0].rank
        
        elif leng == 5:
            if cardlist[0].rank - cardlist[1].rank == 4 and cardlist[1].rank - cardlist[2].rank == 4 and cardlist[2].rank - cardlist[3].rank ==4\
                       and cardlist[3].rank - cardlist[4].rank ==4 and cardlist[3].number != 12 and cardlist[2].number != 13:
       
                maxr = cardlist[0].rank *10000
                matchrule = True
                level = 5
                    
            elif cardlist[0].rank - cardlist[1].rank == 4 and cardlist[1].rank - cardlist[2].rank == 36 and cardlist[2].rank - cardlist[3].rank ==4\
                       and cardlist[3].rank - cardlist[4].rank ==4 and cardlist[0].number == 15 and cardlist[1].number == 14:
 
                maxr = cardlist[0].rank *10000
                matchrule = True
                level = 5
                cardlist[0].rect,  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect =\
                       cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect, cardlist[0].rect,  cardlist[1].rect

                
            elif cardlist[0].rank - cardlist[1].rank == 36 and cardlist[1].rank - cardlist[2].rank == 4 and cardlist[2].rank - cardlist[3].rank ==4\
                       and cardlist[3].rank - cardlist[4].rank ==4 and cardlist[0].number == 15 and cardlist[1].number == 6:
                
           
                maxr = cardlist[0].rank *10000
                matchrule = True
                level = 5
                cardlist[0].rect,  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect=\
                                  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect,  cardlist[0].rect

                
            elif cardlist[0].number - cardlist[1].number ==1 and cardlist[1].number - cardlist[2].number ==1 and \
                    cardlist[2].number - cardlist[3].number ==1 and cardlist[3].number - cardlist[4].number ==1 and\
                    cardlist[3].number != 12 and cardlist[2].number != 13:
                 
        
                    maxr = cardlist[0].rank *1
                    matchrule = True
                    level = 1
                    
            

   
            elif cardlist[0].number  == 15 and cardlist[1].number  == 6 and cardlist[2].number ==5 \
                     and cardlist[2].number  == 4 and cardlist[2].number == 3:
                 
                maxr = cardlist[0].rank *1
                matchrule = True
                level = 1
                cardlist[0].rect,  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect=\
                                  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect,  cardlist[0].rect  
              
                        
            
            elif cardlist[0].number  == 15 and cardlist[1].number == 14 and cardlist[2].number ==5  \
                     and cardlist[3].number == 4 and cardlist[4].number== 3:
   
                maxr = cardlist[0].rank *1
                matchrule = True
                level = 1
                cardlist[0].rect,  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect =\
                       cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect, cardlist[0].rect,  cardlist[1].rect 
                        
     

            elif cardlist[0].suit == cardlist[1].suit == cardlist[2].suit == cardlist[3].suit == cardlist[4].suit:
          
                maxr = cardlist[0].rank *10
                matchrule = True
                level = 2
 
            
            elif cardlist[0].number == cardlist[1].number  == cardlist[2].number == cardlist[3].number:
             
                maxr = cardlist[0].rank *1000
                level = 4
                matchrule = True
                 
                
            elif cardlist[1].number == cardlist[2].number == cardlist[3].number == cardlist[4].number:
    
                maxr = cardlist[1].rank *1000
                level = 4
                matchrule = True
                 
                cardlist[0].rect,  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect=\
                                  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect,  cardlist[0].rect                       

                        
            elif cardlist[0].number == cardlist[1].number == cardlist[2].number and cardlist[3].number == cardlist[4].number :
               
                maxr = cardlist[0].rank *100
                level = 3
                matchrule = True
               
                

            elif cardlist[0].number == cardlist[1].number and cardlist[2].number == cardlist[3].number == cardlist[4].number :
              
                maxr = cardlist[2].rank *100
                level = 3
                matchrule = True
                
                cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect, cardlist[0].rect,  cardlist[1].rect =\
                        cardlist[0].rect,  cardlist[1].rect,  cardlist[2].rect,  cardlist[3].rect,  cardlist[4].rect
 
        else:
            matchrule = False
     
 
    return leng, maxr, level, matchrule

  




def afterplay0(beforecardlist, aftercardlist, w, card_hgt):
    width, height = main.width, main.height
    if aftercardlist:
        aftercardlist = sortingnumber(aftercardlist)
        centerys = [y.rect.center for y in aftercardlist]    
        for i in range(len(aftercardlist)):       
            aftercardlist[i].rect.center = w[len(aftercardlist)-1][i], height -10 - card_hgt//2         
            screen.blit(aftercardlist[i].image, aftercardlist[i].rect)
             
            pygame.display.update()
 
    return aftercardlist

    
def afterplay1(beforecardlist, aftercardlist, h, card_wid):
    width, height = main.width, main.height
    if aftercardlist:
        aftercardlist = sortingnumber(aftercardlist)    
        for i in range(len(aftercardlist)):
            aftercardlist[i].rect.center = width -10 - card_wid//2, h[len(aftercardlist)-1][i]
            screen.blit(aftercardlist[i].image, aftercardlist[i].rect)
            
            pygame.display.update()
 
    return aftercardlist


def afterplay3(beforecardlist, aftercardlist, h, card_wid):
    width, height = main.width, main.height
    if aftercardlist:
        aftercardlist = sortingnumber(aftercardlist)    
        for i in range(len(aftercardlist)):
            aftercardlist[i].rect.center = 10+ card_wid//2, h[len(aftercardlist) - 1][i]
            screen.blit(aftercardlist[i].image, aftercardlist[i].rect)
       
            pygame.display.update()
 
    return aftercardlist

def afterplay2(beforecardlist, aftercardlist, w, card_hgt):
    width, height = main.width, main.height
    if aftercardlist:
        aftercardlist = sortingnumber(aftercardlist)
        for i in range(len(aftercardlist)):
            aftercardlist[i].rect.center = w[len(aftercardlist) - 1][i], 10 + card_hgt//2        
            screen.blit(aftercardlist[i].image, aftercardlist[i].rect)
            
            pygame.display.update()
 
    return aftercardlist

#出牌函数
def play(playerc, selectc, ondesk, discard, w, height, screen):
  
    ondesk.clear()
    for each in selectc:      
        discard.append(each)
        ondesk.append(each)
        playerc.remove(each)         
    selectc.clear()

    ondesk = sortingnumber(ondesk)
    
    for i in range(len(ondesk)): 
        ondesk[i].rect.center = w[len(ondesk) -1][i], height//2
        ondesk[i].image = pygame.image.load(os.path.join("image", str(ondesk[i].rank)+".jpg"))
        screen.blit(ondesk[i].image, ondesk[i].rect)
        
        pygame.display.update()
        
    return playerc, selectc, ondesk, discard
 
  

def sortingnumberee(cardlist):
 
    if not cardlist:
        pass
    else:
        #找出所有的左坐标
        lefts = [e.rect.left for e in cardlist]
        tops = [e.rect.top for e in cardlist]
     
        #开始20次循环排列
        for s in range(20):
            for i in range(len(cardlist)-1):
                if cardlist[i].rank < cardlist[i+1].rank:
                    cardlist[i], cardlist[i+1] = cardlist[i+1], cardlist[i]
                    
        #用新的cardlist重载cardlist，将所有的左坐标贴上，然后重新显示
        
 
        for j in range(len(cardlist)):
 
            cardlist[j].rect.left = lefts[j]
            cardlist[j].rect.top= tops[j]
            cardlist[j].chosen = False 
            screen.blit(cardlist[j].image, cardlist[j].rect)
                                     
            pygame.display.update()
     
        return cardlist

  
def sortingnumber(cardlist):
 
    if not cardlist:
        pass
    else: 
        #找出所有的左坐标
        lefts = [e.rect.left for e in cardlist]
        tops = [e.rect.top for e in cardlist] 
        
        #开始20次循环排列
        for s in range(20):
            for i in range(len(cardlist)-1):
                if cardlist[i].rank < cardlist[i+1].rank:
                    cardlist[i], cardlist[i+1] = cardlist[i+1], cardlist[i]
                    
        #用新的cardlist重载cardlist，将所有的左坐标贴上，然后重新显示  
        for j in range(len(cardlist)):
 
            cardlist[j].rect.left = lefts[j]
            cardlist[j].rect.top= max(tops)
            cardlist[j].chosen = False 
            screen.blit(cardlist[j].image, cardlist[j].rect)
                                     
            pygame.display.update()
     
        return cardlist

#加了ee的是电脑用的
def sortingsuitee(cardlist):
 
    #找出所有的左坐标
    lefts = [e.rect.left for e in cardlist]
    tops = [e.rect.top for e in cardlist] 
    
    if not cardlist:
        pass
    else: 
        a, b, c, d, e = [], [], [], [], []
        for eacha in cardlist:
            if eacha.suit == "Spade":
                a.append(eacha)
            elif eacha.suit == "Heart":
                b.append(eacha)
            elif eacha.suit == "Club":
                c.append(eacha)
            else:
                d.append(eacha)
                
        a = sortingnumber(a)
        b = sortingnumber(b)
        c = sortingnumber(c)
        d = sortingnumber(d)
        if a:
            e.extend(a)
        if b:
            e.extend(b)
        if c:
            e.extend(c)
        if d:
            e.extend(d)
        for j in range(len(cardlist)): 
            e[j].rect.left = lefts[j]
            e[j].rect.top = tops[j]             
            e[j].chosen = False              
            screen.blit(e[j].image, e[j].rect)
            
            pygame.display.update()
        return e

  
def sortingsuit(cardlist):
    
    if not cardlist:
        pass    
    else:        
        #找出所有的左坐标、顶坐标，用来更新/归零牌的位置
        lefts = [e.rect.left for e in cardlist]
        tops = [e.rect.top for e in cardlist]
     
        a, b, c, d, e = [], [], [], [], []
        for eacha in cardlist:
            if eacha.suit == "Spade":
                a.append(eacha)
            elif eacha.suit == "Heart":
                b.append(eacha)
            elif eacha.suit == "Club":
                c.append(eacha)
            else:
                d.append(eacha)
                
            for s in range(6):
                for i in [a, b, c, d]:
                    for each in range(min(len(a), len(b), len(c), len(d))-1):
                        if i[each].rank < i[each+1].rank:
                            i[each+1], i[each] = i[each], i[each+1]                  
  
        if a:
            e.extend(a)
        if b:
            e.extend(b)
        if c:
            e.extend(c)
        if d:
            e.extend(d)
        #用新的cardlist重载cardlist，将所有的左坐标贴上，然后重新显示
 
        for j in range(len(e)):
            e[j].rect.left = 0
            e[j].rect.top = 0
            e[j].rect.top = max(tops)
            e[j].rect.left = lefts[j]            
            e[j].chosen = False
            screen.blit(e[j].image, e[j].rect)            
                                     
            pygame.display.update()
        return e


 

 
def turn_ai (playerc, selectc, ondesk,  canplayc, started, currentplayer, discard, w, height, screen, playedsituation):
     
   
    playerc = sortingnumber(playerc)
    pygame.display.update()
    fuckplayedsituation = playedsituation.copy()
    fuck2playedsituation = playedsituation.copy()
    selectc.clear()

    
    if len(playerc) > 5:
        d = random.randint(1, 5)
    else:
        d = random.randint(1, len(playerc))

        
    if len(playerc) > 4:
        b = random.randint(0, 4)
    else:
        b = random.randint(0, len(playerc))

    if started == False:
 
        a = 100
        while True:
            fuckplayerc = playerc.copy()
            fuckplayerc.remove(card.diamond3)
            selectc.clear()
            selectc.append(card.diamond3)
            selectc.extend(random.sample(fuckplayerc, b))
            canplayc = ifcanplay(selectc, ondesk, canplayc, started)
            if canplayc == True:
                playerc, selectc, ondesk, discard = play(playerc, selectc, ondesk, discard, w, height, screen)
              
                playedsituation[currentplayer] = 1
                break
            a -= 1
            if a == 0:
                break
        if canplayc == False:
          
            selectc.clear()
            selectc.append(card.diamond3)
            playerc, selectc, ondesk, discard = play(playerc, selectc, ondesk, discard, w, height, screen)
            playedsituation[currentplayer] = 1
        currentplayer +=4

            
    elif started == True:
 
        fuckplayedsituataion = playedsituation.copy()
        fuckplayedsituation.remove(playedsituation[currentplayer])
        
        if fuckplayedsituation == [0,0,0]:
            playedsituation = [5,5,5,5] 
            ondesk.clear()           
      
            a = 100
            while True:
                fuckplayerc = playerc.copy()                 
                selectc.clear()
                selectc.extend(random.sample(playerc, d))
                canplayc = ifcanplay(selectc, ondesk, canplayc, started)
                if canplayc == True:
                    playerc, selectc, ondesk, discard = play(playerc, selectc, ondesk, discard, w, height, screen)
                  
                    playedsituation[currentplayer] = 1
                    break
                a -= 1
                if a == 0:
                    break
                
            if canplayc == False:              
                selectc.clear()
                selectc.append(random.choice(playerc))
                playerc, selectc, ondesk, discard = play(playerc, selectc, ondesk, discard, w, height, screen)
                playedsituation[currentplayer] = 1



        
        else:
            if len(playerc) >= len(ondesk):
                a = 100
                while True:
                    fuckplayerc = playerc.copy()
                    selectc.clear() 
                    selectc.extend(random.sample(fuckplayerc, len(ondesk)))
                    canplayc = ifcanplay(selectc, ondesk, canplayc, started)
                    if canplayc == True:
                   
                        playerc, selectc, ondesk, discard = play(playerc, selectc, ondesk, discard, w, height, screen)
                        playedsituation[currentplayer] = 1
                        break
                    
                    a -= 1
                    if a == 0:
                        break
                if canplayc == False:
                    playedsituation[currentplayer] = 0
                    
            elif len(playerc) < len(ondesk):
                playedsituation[currentplayer] = 0
      
            
        

        
 
    selectc.clear()
    
    pygame.display.update()
     
 

    return playerc, selectc, ondesk,  canplayc, started, currentplayer, discard, playedsituation

  
