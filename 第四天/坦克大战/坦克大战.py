#!/usr/bin/python
#encoding=utf-8
import pygame
import sys
from pygame.locals import*
#坦克大战主界面
class TankScreen(object):
    #开始游戏
    def startGame(self):# {{{
        pygame.init()#初始化，加载系统资源
    #创建一个屏幕，屏幕的大小（宽,高），窗口特性（RESIEBLE可变和0不可变,FULLSCREEN）
        screen=pygame.display.set_mode((300,400),0,32)
        pygame.display.set_caption("坦克大战")# }}}
    #color RGB(0,0,0)黑色]
        while True:
            screen.fill((255,255,255))#设置背景色为黑色
            self.get_event()
            screen.blit(self.write_text(),(0,5))
            pygame.display.update()
    def stopGame(self):
        sys.exit()


    def settitle(self):
        pass

    #在屏幕上显示文字
    def write_text(self):
        font=pygame.font.SysFont("simsunextb",10)#定义一个字体
        test_sf=font.render('地方坦克数量5',True,(255,0,255))#根据文字创建一个文件的图像
        return test_sf

    def get_event(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                self.stopGame()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    pass
                if event.key==K_DOWN:
                    pass
                if event.key==K_LEFT:
                    pass
                if event.key==K_RIGHT:
                    pass
                if event.key==K_ESCAPE:
                    self.stopGame()


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
            #所有对象共有的属性

class Tank(BaseItem):
    width=50
    heigh=50
    def __init__(self,screen,top,left):
        super().__init__()
        self.screen=screen
        self.direction="D"
        self.images["L"]=pygame.image.load("\image\tank,gif")
        self.image=self.images[self.direction]
        self.live=True
            #坦克行为，把坦克显示在窗口上
        self.rect=self.image.rect()
        self.rect.left=left
        self.rect.top=top
    def display(self):
        self.image=self.image[self.direction]
        self.screen.blit(self.image,self.rect)

if __name__ == '__main__':
    tank_screen=TankScreen()
    tank_screen.startGame()

