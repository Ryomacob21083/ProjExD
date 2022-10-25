import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")    ##タイトルバーに「初めての...」を表示
    scrn_sfc = pg.display.set_mode((1600, 900)) ## 800×600の画面surfaceを生成
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    clock = pg.time.Clock()

    #練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        scrn_sfc.blit(tori_sfc, tori_rct)
        pg.display.update()
        clock.tick(0.2)
    
    

if __name__ == "__main__":
    pg.init()           ##モジュールを初期化
    main()
    pg.quit()           ##モジュールの初期化を解除
    sys.exit()          ##プログラムを終了
