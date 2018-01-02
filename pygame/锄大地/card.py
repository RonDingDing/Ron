import random
import os.path
import pygame
import sys

#定义每一张牌
    
class Card(pygame.sprite.Sprite):
    def __init__ (self, bg_size, image, rank, suit, number, chosen=False):
        pygame.sprite.Sprite.__init__(self)

        self.screenwidth,  self.screenheight = bg_size[0], bg_size[1]
        self.image = pygame.image.load(image)
        self.rank = rank
        self.suit = suit
        self.number = number
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (self.screenwidth - self.rect.width)//2, \
                                        (self.screenheight - self.rect.height)//2
        self.chosen = chosen
        

        
        
 
#定义牌堆的数据
rank = [x for x in range(1, 53)]
suit = [y for y in ["Diamond","Club","Heart","Spade"]*13]
number = sorted([(z%13+3) for z in range(52)])
 
cardso = ([{"Rank": rank[x], "Suit": suit[x], \
           "Number":number[x]} for x in range(len(rank))])
bg_size = 800, 600


#创造牌堆
pile =[]
for i in range(52):    
    pile.append(Card(bg_size, os.path.join("image", "blank.png"), \
                    cardso[i]["Rank"], cardso[i]["Suit"], cardso[i]["Number"]))
diamond3 = pile[0]
