import tkinter as tk
import pygame as pg
import sys

stand = 0  ##０なら地面にいる
vy = 0.05  ##重力加速度
def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def check_stand(y): ##地面にいるかを判定する
        global stand, vy
        if y >= 420:
            stand = 0
            y = 420
            vy = 0
        else:
            stand = 1
        return y


class Screen:
    def __init__(self, title, wh, bg_png):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bg_png)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        

class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def getCoord(self):
        return(self.x-self.w/2, self.y-self.h/2, self.x+self.w, self.y+self.h/2)

    def draw(self, scr:Screen):
        for i in range(1):
            pg.draw.rect(scr, (116, 80, 48), self.getCoord())



class Bird:
    global stand
    key_delta = {
        pg.K_UP:    [0, -5],
        pg.K_DOWN:  [0, 0],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0], 
    }
    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        global vy
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound_wh(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        check_stand(self.rct.bottom)
        if stand == 1:
            self.rct.centery += vy
        vy += 0.05
        self.blit(scr)


def check_bound_wh(obj_rct, scr_rct):
    global vy
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom - 50 < obj_rct.bottom:
        tate = -1
        vy = 0    ##地面についた際に重力加速度をリセット
    return yoko, tate


def main():
    scr = Screen("ActionGame", (800, 480), "ex06/images/action.png")
    bird = Bird("ex06/images/0.png", 1.0, (100, 300))
    block = Block(400, 150, 5, 5)
    block.draw(scr.sfc)
    pg.draw.rect(scr.sfc, (255, 255, 255), (750, 100, 5, 320))
    clock = pg.time.Clock()
    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        block.draw(scr.sfc)
        pg.draw.rect(scr.sfc, (255, 255, 255), (750, 100, 5, 320))
        
        bird.update(scr)
        pg.display.update()
        clock.tick(1000)
if __name__ == "__main__":
    pg.init()           ##モジュールを初期化
    main()
    pg.quit()           ##モジュールの初期化を解除
    sys.exit()          ##プログラムを終了
    