import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct): #練習７
    #obj_rct:こうかとんrectまたは爆弾rect
    #scr_rct:スクリーンrect

    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main(): #練習１
    pg.display.set_caption("逃げろ！こうかとん")    ##タイトルバーに「初めての...」を表示
    scrn_sfc = pg.display.set_mode((1600, 900)) ## 800×600の画面surfaceを生成
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    #練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #練習5
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    #練習6
    vx, vy = +1, +1


    clock = pg.time.Clock()
    while True: #練習２
        scrn_sfc.blit(bg_sfc, bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_states = pg.key.get_pressed() #練習4
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)   #練習7
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1

        scrn_sfc.blit(tori_sfc, tori_rct) #練習３
        yoko, tate = check_bound(bomb_rct, scrn_rct)#練習7
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy)          #練習６
        scrn_sfc.blit(bomb_sfc, bomb_rct) #練習５

        #練習８
        if tori_rct.colliderect(bomb_rct):
            return
        pg.display.update()
        clock.tick(1000)
    
    

if __name__ == "__main__":
    pg.init()           ##モジュールを初期化
    main()
    pg.quit()           ##モジュールの初期化を解除
    sys.exit()          ##プログラムを終了
